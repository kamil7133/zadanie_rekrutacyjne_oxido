import os
from openai import OpenAI
from pathlib import Path

class ArticleProcessor:
    def __init__(self, api_key):
        """
        Inicjalizacja procesora artykułów.

        Args:
            api_key (str): Klucz API OpenAI
        """
        self.client = OpenAI(api_key=api_key)

    def read_article(self, file_path):
        """
        Odczytuje zawartość artykułu z pliku.

        Args:
            file_path (str): Ścieżka do pliku z artykułem

        Returns:
            str: Zawartość artykułu
        """
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()

    def process_with_ai(self, article_content):
        """
        Przetwarza artykuł przez API OpenAI.

        Args:
            article_content (str): Treść artykułu

        Returns:
            str: Wygenerowany kod HTML
        """
        prompt = """
        Przekształć poniższy artykuł w kod HTML spełniający następujące wymagania:
        1. Użyj odpowiednich tagów HTML do strukturyzacji treści (np. h1, h2, p, article, section itp.)
        2. W każdej sekcji artykułu zidentyfikuj co najmniej jedno miejsce, gdzie warto dodać obrazek.
           - Dodaj tagi img z:
             - src="image_placeholder.jpg"
             - atrybutem alt zawierającym dokładny prompt do wygenerowania grafiki
             - podpisem pod grafiką używając odpowiedniego tagu HTML (figcaption)
        3. Nie dodawaj kodu CSS ani JavaScript
        4. Nie dodawaj tagów html, head, body - zwróć tylko zawartość do umieszczenia między tymi tagami

        Oto artykuł do przetworzenia:

        {content}
        """

        response = self.client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Jesteś ekspertem w konwersji tekstu na semantyczny kod HTML."},
                {"role": "user", "content": prompt.format(content=article_content)}
            ],
            max_tokens=1500,
            temperature=0.7
        )

        return response.choices[0].message.content.strip()

    def save_html(self, html_content, output_file):
        """
        Zapisuje wygenerowany kod HTML do pliku.

        Args:
            html_content (str): Wygenerowany kod HTML
            output_file (str): Ścieżka do pliku wyjściowego
        """
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(html_content)


def main():
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        raise ValueError("Nie znaleziono klucza API OpenAI. Ustaw zmienną środowiskową OPENAI_API_KEY.")

    processor = ArticleProcessor(api_key)

    input_file = Path("artykul.txt")
    output_file = Path("artykul.html")

    if not input_file.exists():
        raise FileNotFoundError(f"Nie znaleziono pliku {input_file}.")

    try:
        article_content = processor.read_article(input_file)

        html_content = processor.process_with_ai(article_content)

        processor.save_html(html_content, output_file)

        print(f"Sukces! Wygenerowany kod HTML został zapisany w {output_file}")

    except Exception as e:
        print(f"Wystąpił błąd: {e}")


if __name__ == "__main__":
    main()
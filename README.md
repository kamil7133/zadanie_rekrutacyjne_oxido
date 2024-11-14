# Zadanie Rekrutacyjne

## Opis
Aplikacja w Pythonie, która:
1. Łączy się z API OpenAI.
2. Wczytuje plik tekstowy z artykułem.
3. Przetwarza zawartość artykułu na kod HTML przy pomocy modelu GPT-4.
4. Zapisuje wygenerowany kod HTML do pliku `artykul.html`.

Wygenerowany kod HTML spełnia następujące wytyczne:
- Strukturyzuje treść artykułu za pomocą odpowiednich tagów HTML (np. `h1`, `h2`, `p`, `article`, `section`).
- Zawiera tagi `<img>` w miejscach, gdzie można dodać grafiki, z atrybutami `src="image_placeholder.jpg"` i `alt` zawierającym prompt dla generowania obrazu.
- Nie zawiera kodu CSS ani JavaScript.

## Struktura Plików
- `main.py` - kod aplikacji łączącej się z API OpenAI.
- `artykul.txt` - przykładowy plik z treścią artykułu do przetworzenia.
- `artykul.html` - wygenerowany kod HTML.
- `podglad.html` - podgląd struktury HTML z użyciem stylów CSS dla wizualizacji wyników.

## Wymagania
- Python 3.x
- Moduł `openai`
- Klucz API OpenAI (wymagany do połączenia z API)

## Instrukcja Użycia
1. Skopiuj repozytorium na swój lokalny komputer.
2. Zainstaluj zależności:

    ```bash
    pip install openai
    ```

3. Ustaw swój klucz API OpenAI jako zmienną środowiskową:

    ### PowerShell
    ```powershell
    $env:OPENAI_API_KEY = "twój_klucz_api"
    ```

    ### Unix (bash)
    ```bash
    export OPENAI_API_KEY="twój_klucz_api"
    ```

4. Uruchom program:

    ```bash
    python main.py
    ```

5. Wygenerowany kod HTML zostanie zapisany w pliku `artykul.html`.
## Korzystanie z docstringów
Aby wyświetlić pomoc dotyczącą klasy i jej metod, można użyć wbudowanej funkcji `help()` w Pythonie, co pozwoli na skorzystanie z docstringów. Poniżej instrukcja:
1. Uruchom sesję interaktywną Pythona w terminalu lub PowerShellu:
   ```bash
   python
2. Zaimportuj klasę `ArticleProcessor`:
   ```bash
   from main import ArticleProcessor
3. Wywołaj funkcję `help()` dla klasy lub metod, aby zobaczyć dokumentację:
   ```bash
   help(ArticleProcessor)
- Można również wyświetlić docstringi dla poszczególnych metod, np.:
      ```bash
      help(ArticleProcessor.read_article)
      ```
4. Aby wyjść z trybu pomocy, naciśnij `q`.


## Uwagi
- Przykładowy plik `artykul.txt` zawiera artykuł używany do testów.
- Plik `podglad.html` pozwala wizualnie sprawdzić strukturę wygenerowanego kodu HTML z dodanym CSS i JS.

## Licencja
Projekt jest dostępny na licencji MIT.

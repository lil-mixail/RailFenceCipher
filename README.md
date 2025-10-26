# Rail Fence Cipher Tools

Zestaw skryptów do szyfrowania i odszyfrowywania klasycznego szyfru płotkowego (Rail Fence Cipher).

## Funkcjonalności
- Szyfrowanie tekstu jawnego (plik `shuffle_script.py`)
- Odszyfrowywanie szyfru metodą płotkową (plik `deshuffle_script.py`)
- Obsługa parametrów przestawieniowych (liczba „szyn” itp.)

## Struktura projektu
- `src/` — skrypty Python
- `examples/` — przykładowe dane wejściowe i wyjściowe

## Przykład użycia
```bash
python3 src/shuffle_script.py examples/plain.txt 3
python3 src/deshuffle_script.py examples/shuffled.txt 3

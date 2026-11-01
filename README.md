# Grafy i ich zastosowania

Implementacje zestawów 1-6.

## Uruchomienie

Wymagany Python 3.11+. Kod uruchamiamy pod Linuksem lub WSL, zawsze z głównego folderu repo.

Z `uv`:

    uv venv --python-preference only-managed --python 3.14
    source .venv/bin/activate
    uv pip install -r requirements.txt

Python od `uv` ma `tkinter`, więc `plt.show()` otwiera okna z wykresami.

Bez `uv`:

    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt

Programy i testy:

    python -m zestaw_2.euler
    python -m pytest

## Zasady

- Każdy zestaw to osobny pakiet, a wspólny kod importujemy, np. `from zestaw_1.graph import Graph`. Nie kopiujemy kodu między zestawami.
- `networkx` służy tylko do sprawdzania wyników w testach. Algorytmy piszemy sami.

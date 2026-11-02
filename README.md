# Grafy i ich zastosowania

Implementacje zestawów 1-6.

## Uruchomienie

Wymagany Python 3.11+.

Z `uv`:

    uv venv --python-preference only-managed --python 3.14
    source .venv/bin/activate
    uv pip install -r requirements.txt

Bez `uv`:

    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt

Programy uruchamiamy jako moduły:

    python -m zestaw_1.zadanie_3

Polecenia uruchamiamy z głównego folderu repo. Wierzchołki są numerowane od 0. Graf podajemy w cudzysłowie, a jego format musi pasować do wybranego kodowania. Programy nie sprawdzają poprawności grafu, więc każdą krawędź trzeba zapisać zgodnie z kodowaniem. Błędne polecenie (zła liczba argumentów, nieznane kodowanie, brak pliku) kończy się krótkim komunikatem.

## Zestaw 1


Przykłady wywołań z krótkim opisem wyniku są w `zestaw_1/przyklady_wywolan.txt`.

### Zadanie 1: zamiana kodowań

Program dostaje graf w jednym kodowaniu, wypisuje wszystkie trzy i rysuje graf na okręgu. Kończy się po zamknięciu okna.

### Zadanie 2: rysowanie na okręgu

Graf podajemy tak samo jak w zadaniu 1. Program tylko rysuje graf i kończy się po zamknięciu okna.


### Zadanie 3: grafy losowe

Program wypisuje listę sąsiedztwa i rysuje wylosowany graf.


### Klasa Graph i wczytywanie

- `zestaw_1/graph.py`: klasa `Graph` trzyma graf jako listę sąsiedztwa w polu `adjacency_list`.
- Tworzenie grafu: `Graph(lista)`, `Graph.from_adjacency_matrix(macierz)` i `Graph.from_incidence_matrix(macierz)`.
- Zamiana na macierze: `g.to_adjacency_matrix()` i `g.to_incidence_matrix()`. Obie zwracają zwykłe listy list, bez numpy.
- `zestaw_1/wczytywanie.py`: funkcja `read_graph()` czyta z terminala kodowanie i graf (w cudzysłowie albo z pliku) i zwraca `Graph`. Używają jej zadania 1 i 2.



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

Polecenia uruchamiamy z głównego folderu repo. Wierzchołki na wejściu i na wyjściu są numerowane od 1, tak jak w przykładach prowadzącej, a w środku programu od 0. Graf podajemy w cudzysłowie, a jego format musi pasować do wybranego kodowania. Programy nie sprawdzają poprawności grafu, więc każdą krawędź trzeba zapisać zgodnie z kodowaniem. Błędne polecenie (zła liczba argumentów, nieznane kodowanie, brak pliku) kończy się krótkim komunikatem.

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
- `zestaw_1/wczytywanie.py`: funkcja `read_graph()` czyta z terminala kodowanie i graf (w cudzysłowie albo z pliku) i zwraca `Graph`. Używają jej zadania 1 i 2 z zestawu 1 oraz 3 i 6 z zestawu 2.

## Zestaw 2

Przykłady wywołań z krótkim opisem wyniku są w `zestaw_2/przyklady_wywolan.txt`.

- Zadanie 1: ciąg liczb jako argumenty; odpowiedź, czy jest graficzny, a jeśli tak, to zbudowany graf.
- Zadanie 2: liczba randomizacji i ciąg graficzny; graf przed i po randomizacji.
- Zadanie 3: graf jak w zestawie 1; spójne składowe i numer największej.
- Zadanie 4: liczba wierzchołków albo nic; losowy graf eulerowski i jego cykl Eulera.
- Zadanie 5: liczba wierzchołków `n` i stopień `k`; losowy graf `k`-regularny.
- Zadanie 6: graf jak w zestawie 1; czy jest hamiltonowski, a jeśli tak, to cykl Hamiltona.

Każdy program na końcu rysuje graf i kończy się po zamknięciu okna.



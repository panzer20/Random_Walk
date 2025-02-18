Language:
English

Project name:
Random walk

Description:
This is a modified version of the program from the book by Eric Matthes entitled: "Python Crash Course: A Hands-On, Project-Based Introduction to Programming" published in 2023 by No Starch Press. The program is used to generate many random walks, i.e. paths without a clear direction, which is determined by a series of random decisions, and their outcome is completely unpredictable,
which can be used, among others, to model particles in a liquid or gas, in stochastic processes, to model stock prices and financial markets.

Installation:
To run the program, you must:
1. Install the latest version of Python.
2. Clone the repository by entering the following command in shell: git clone https://github.com/panzer20/Random_Walk.git
3. Create a virtual environment by entering the following command in the shell: python3 -m venv your_folder_name and then activate it in the shell using the command:
a) In Linux/macOS:
source environment_name/bin/activate
b) In Windows:
source environment_name/Scripts/activate
4. In a shell, go to the folder where the cloned repository is located and type the command: pip install -r requirements.txt
5. Open the file: wizacja_bladzenie_losowego.py

Usage:
In the file `wizualizacja_bladzenia_losowego.py` in the argument of the `RandomWalk` class (line 8) we provide the number of points to be generated as part of the random walk.
In the function `plt.style.use` (line 12) as an argument we can provide one of the available chart styles in `matplotlib`.
The value of the `figsize` argument of the `plt.subplots` function (line 12) can be any two numbers that specify the width and height of the chart window in inches.
In the function `ax.scatter` (line 15) as the value of the `c` argument we can provide the name of the color in English format (e.g. `'red'`, `'blue'`, etc.), or if we want to use a color map, we can leave the default value of `point_numbers`. Additionally, in the `cmap=plt.cm.` argument we can specify the name of the color map (e.g. `plt.cm.Blues`).
The `s` argument in the `ax.scatter` function (in line 15) is used to determine the size of all dots on the graph.
The values ​​of the `c` and `s` arguments in the `ax.scatter` function in line 19 refer to the first point of the random walk, where:
- `c` is the color of the first point,
- `s` is its size.
Similarly, in the `ax.scatter` function in line 20, the arguments work analogously, but refer to the last point of the walk.
After generating the random walk graph, it is possible to save it to disk. To do this, click on the floppy disk icon in the lower left corner of the graph, and then select the location where you want to save the file.

Screenshots:

![Screenshot](./screenshots/Random_Walk.PNG)

License:
MIT License


Język:
Polski

Nazwa projektu: 
Błądzenie losowe

Opis: 
Jest to zmodyfikowana wersja programu z książki autorstwa Eric Matthes pod tytułem: "Python Crash Course: A Hands-On, Project-Based Introduction to Programming" wydanej w 2023 roku przez wydawnictwo No Starch Press. Program służy do generowania wielu błądzeń losowych, czyli ścieżek pozbawionych wyraźnego kierunku, który jest ustalany na podstawie serii losowych decyzji, a ich wynik jest całkowicie nieprzewidywalny,
co może być wykorzystywane m.in. do modelowania cząsteczek w cieczy lub gazie, w procesach stochastycznych, do modelowania cen akcji i rynków finansowych.

Instalacja: 
W celu uruchomienia programu należy:
1. Zainstalować najnowszą wersję programu Python.
2. Sklonować repozytorium przez wpisanie w powłoce polecenia: git clone https://github.com/panzer20/Random_Walk.git
3. Utworzyć środowisko wirtualne przez wprowadzenie w powłoce polecenia: python3 -m venv nazwa_twojego_folderu a następnie aktywować je w powłoce za pomocą polecenia:
a) W Linux/macOS:
source nazwa_środowiska/bin/activate
b) W Windows:
source nazwa_środowiska/Scripts/activate
4. Przejść w powłoce do folderu, w którym znajduje się sklonowane repozytorium i wprowadzić komendę: pip install -r requirements.txt
5. Otworzyć plik: wizualizacja_bladzenie_losowego.py

Użycie: 
W pliku `wizualizacja_bladzenia_losowego.py` w argumencie klasy `RandomWalk` (w 8. linii) podajemy liczbę punktów, które mają zostać wygenerowane w ramach błądzenia losowego. 
W funkcji `plt.style.use` (w 12. linii) jako argument możemy podać jeden z dostępnych stylów wykresów w `matplotlib`. 
Wartość argumentu `figsize` funkcji `plt.subplots` (w 12. linii) może być dowolnymi dwoma liczbami, które określają szerokość i wysokość okna wykresu w calach.
W funkcji `ax.scatter` (w 15. linii) jako wartość argumentu `c` możemy podać nazwę koloru w formacie angielskim (np. `'red'`, `'blue'`, itp.), lub jeśli chcemy użyć mapy kolorów, możemy pozostawić domyślną wartość `point_numbers`. Dodatkowo, w argumencie `cmap=plt.cm.` możemy podać nazwę mapy kolorów (np. `plt.cm.Blues`).
Argument `s` w funkcji `ax.scatter` (w 15. linii) służy do określenia wielkości wszystkich kropek na wykresie.
Wartości argumentów `c` i `s` w funkcji `ax.scatter` w 19. linii dotyczą pierwszego punktu błądzenia losowego, gdzie:
- `c` to kolor pierwszego punktu,
- `s` to jego wielkość.
Podobnie, w funkcji `ax.scatter` w 20. linii, argumenty działają analogicznie, ale dotyczą ostatniego punktu błądzenia.
Po wygenerowaniu wykresu błądzenia losowego, istnieje możliwość zapisania go na dysku. W tym celu należy kliknąć na ikonę dyskietki w lewym dolnym rogu wykresu, a następnie wybrać lokalizację, w której chcemy zapisać plik.

Screenshots:

![Screenshot](./screenshots/Random_Walk.PNG)

Licencja:
MIT License

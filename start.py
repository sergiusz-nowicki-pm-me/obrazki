# 1. Pobrać ścieżkę z wiersza poleceń
#   1.1 obpalać program z katalogu roboczego (w którym są pliki) nie podająć parametru - AUTOMATYCZNIE 
#   1.2 odpalić z dowolnego katalogu i podać ściezkę w parametrze - 
# 2. Wylistować zawartość katalogu i wybrać pliki graficzne.
# 3. Wczytań wybrane pliki po kolei i przetworzyć
# 4. Zapisać pliki do podkatalogu

import sys
import os
import imageio

sciezka = "."
obslugiwaneTypyPlikow = ['.jpg', '.jpeg', '.png']

if len(sys.argv) > 1:
    for paramNum in range(1, len(sys.argv)):
        print("Wczytuje parametr", paramNum, f'o wartości "{sys.argv[paramNum]}"')
        if sys.argv[paramNum].startswith("-p="):
            sciezka = sys.argv[paramNum][3:];
            print(f'Podano ścieżkę do katalogu ropboczego "{sciezka}"')
        else:
            print(f'Podano nieobsługiwany typ parametru "{sys.argv[paramNum]}"')

zawartoscKatalogu = [wpis for wpis in os.listdir(sciezka) if os.path.isfile(os.path.join(sciezka, wpis))]
print("pliki w katalogu", zawartoscKatalogu)
plikiGraficzne = [wpis for wpis in zawartoscKatalogu if wpis[wpis.rfind('.'):] in obslugiwaneTypyPlikow]
print("pliki graficzne w katalogu", plikiGraficzne)

for imageFile in plikiGraficzne:
# 1. Pobrać ścieżkę z wiersza poleceń
#   1.1 obpalać program z katalogu roboczego (w którym są pliki) nie podająć parametru - AUTOMATYCZNIE 
#   1.2 odpalić z dowolnego katalogu i podać ściezkę w parametrze - 
# 2. Wylistować zawartość katalogu i wybrać pliki graficzne.
# 3. Wczytań wybrane pliki po kolei i przetworzyć
# 4. Zapisać pliki do podkatalogu
# 5. Dodać wybór operacji


import sys
import os
import imageio
import PIL

conversion = None
resize = None
rotate = None

sciezkaKataloguWyjsciowego = 'tmp'
sciezka = "."
obslugiwaneTypyPlikow = ['.jpg', '.jpeg', '.png']

if len(sys.argv) > 1:
    for paramNum in range(1, len(sys.argv)):
        print("Wczytuje parametr", paramNum, f'o wartości "{sys.argv[paramNum]}"')
        if sys.argv[paramNum].startswith("-p="):
            sciezka = sys.argv[paramNum][3:]
            print(f'Podano ścieżkę do katalogu roboczego "{sciezka}"')
        elif sys.argv[paramNum].startswith("-o="):
            sciezkaKataloguWyjsciowego = sys.argv[paramNum][3:]
            print(f'Podano ścieżkę do katalogu wyjscia "{sciezkaKataloguWyjsciowego}"')
        elif sys.argv[paramNum].startswith("-c="):
            conversion = sys.argv[paramNum][3:]
            print(f'Podano wartość konwersji')
        elif sys.argv[paramNum].startswith("-s="):
            tekst = sys.argv[paramNum][3:].split(":")
            if len(tekst) != 2:
                print("Podano bledny wymiar -s= . Nalezy podac szerokosc:wysokosc")
                exit()
            szerokosc,wysokosc = tekst
            try:
                resize = (int(szerokosc),int(wysokosc))
            except:
                print("Wymiary musza byc liczba calkowita")
                exit()
            print(f'Podano ścieżkę do katalogu wyjscia "{sciezkaKataloguWyjsciowego}"')
        else:
            print(f'Podano nieobsługiwany typ parametru "{sys.argv[paramNum]}"')
os.chdir(sciezka)
zawartoscKatalogu = [wpis for wpis in os.listdir(".") if os.path.isfile(wpis)]
print("pliki w katalogu", zawartoscKatalogu)
plikiGraficzne = [wpis for wpis in zawartoscKatalogu if wpis[wpis.rfind('.'):] in obslugiwaneTypyPlikow]
print("pliki graficzne w katalogu", plikiGraficzne)


# index = 0
# while True:
#     if index > 0:
#         katalogWyjsciowy = os.path.join(sciezka, nazwaKataloguWyjsciowego + str(index))
#     else:
#         katalogWyjsciowy = os.path.join(sciezka, nazwaKataloguWyjsciowego)
#     index += 1

    # if os.path.exists(katalogWyjsciowy):
    #     continue
    # else:
    #     os.mkdir(katalogWyjsciowy)
    #     break
if not os.path.exists(sciezkaKataloguWyjsciowego):
    os.makedirs(sciezkaKataloguWyjsciowego)

for imageFile in plikiGraficzne:
    img = imageio.v3.imread(imageFile)
    image = PIL.Image.fromarray(img)
    if resize != None:
        image = image.resize(resize)
    if conversion != None:
        image = image.convert(conversion)  
    # image.show()
    image.save(os.path.join(sciezkaKataloguWyjsciowego, imageFile))
   # imageio.v3.imwrite(os.path.join(katalogWyjsciowy, imageFile + '.png'), img)
#ZADANIE 1
imie = input("Podaj swoje imię: ")
wiek = int(input("Podaj swój wiek: "))
rok = 2023
rok_python = 1991
wiek_python = rok - rok_python

if wiek > wiek_python:
    x = "starszy"
else:
    x = "młodszy"

print("Mów mi Python, mam ", wiek_python ," lata. Witaj w moim świecie ", imie , ". Jesteś " , x , " ode mnie.")


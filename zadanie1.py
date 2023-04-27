import datetime

#zadanie 1
print("podaj imię:")
imie=input()
print("podaj swój wiek:")
wiek=int(input())
dzisiaj = datetime.date.today()
rok=dzisiaj.year

if wiek>rok:
    print("Mów mi Python mam 32 lata. Witaj w moim świecie", imie, "Jesteś starszy ode mnie")
else:
    print("Mów mi Python mam 32 lata. Witaj w moim świecie", imie, "Jesteś młodszy ode mnie")
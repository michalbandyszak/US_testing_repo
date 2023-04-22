import datetime

dane_uzytkownika = input("Po spacjach podaj imię i wiek: ").split()
python_age = datetime.date.today().year - 1991
if int(dane_uzytkownika[1]) < python_age:
    print(f"Mów mi python, mam {python_age} lat. Witaj w moim świecie {dane_uzytkownika[0]}. Jesteś młodszy ode mnie")
else:
    print(f"Mów mi python, mam {python_age} lat. Witaj w moim świecie {dane_uzytkownika[0]}. Jesteś starszy ode mnie")

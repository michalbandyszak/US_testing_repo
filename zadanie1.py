
imie = str(input("Hej! Podaj swoje imie: "))
wiek = int(input("Jeszcze podaj wiek:  "))

if wiek > 32:
    print("Mów mi Python, mam 32 lata. Witaj w moim świecie " + (imie) + ". Jesteś starszy ode mnie.")
elif wiek < 32:
    print("Mów mi Python, mam 32 lata. Witaj w moim świecie " + (imie) + ". Jesteś młodszy ode mnie.")
else:
    print("Mów mi Python, mam 32 lata. Witaj w moim świecie " + (imie) + ". Jesteśmy w tym samym wieku!.")
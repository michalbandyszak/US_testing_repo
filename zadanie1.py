imie = input("Jak masz na imię dobry człowieku? ")
wiek = int(input("Ile masz lat dobry człowieku? "))
pythonWiek = 32
wynik = 32 - wiek
if(wynik > 0):
    ktoStarszy = "młodszy"
else:
    ktoStarszy = "starszy"

print("Mów mi Python, mam" , pythonWiek , "lat/a. Witaj w moim świecie " + imie + " jesteś " + ktoStarszy + " ode mnie.")
name = input("Proszę podaj swoje imię: ")
age = int(input("Podaj swój wiek: "))
python_age = 2023 - 1994
difference = python_age - age
if(difference > 0):
    sentence = "młodsza ode mnie"
elif(difference < 0):
    sentence = "starsza ode mnie"
else:
    sentence = "w tym samym wieku co ja"

print("Mów mi Python, mam 29 lat. Witaj w moim świecie " + name + "! Jesteś " + sentence + " :).")

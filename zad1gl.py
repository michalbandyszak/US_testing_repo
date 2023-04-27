imie = input('Jak się nazywasz? ')
wiek = int(input('Ile masz lat? '))
aktRok = 2023
pythonRok = 1991
wiekPythona = aktRok - pythonRok
print("Witaj", imie)
print("Mów mi Python, mam", wiekPythona, "lat.")
if wiek > wiekPythona:
    print('Jesteś starszy ode mnie.')
else:
    print('Jesteś młodszy ode mnie.')
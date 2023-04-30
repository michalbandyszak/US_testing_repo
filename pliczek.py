aktualny_rok = 2023
python_rok = 1991

a = input('Wpisz swoje imię')
b = int(input('Wpisz swój wiek'))

py_wiek = aktualny_rok - python_rok

print("Witaj", a + "!")
print('Mów mi python, mam', py_wiek, "lata.")

if b > py_wiek:
    print("Jestes starszy ode mnie.")
else:
    print("Jestes mlodszy ode mnie.")
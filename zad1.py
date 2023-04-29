name = input("Podaj swoje imię: ")
age = int(input("Podaj swój wiek: "))

year = 2023
year_python = 1991
my_age = year - year_python

if my_age > age:
    print(f"Mów mi Python, mam {my_age} lata. Witaj w moim świecie {name}. Jesteś młodszy/a ode mnie.")    
else:
    print(f"Mów mi Python, mam {my_age} lata. Witaj w moim świecie {name}. Jesteś starszy/a ode mnie.")

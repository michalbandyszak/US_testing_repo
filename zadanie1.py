
name = input("Podaj imie: ")
age = int(input("Podaj wiek: "))
python_age = 2023 - 1991
print(python_age)
print(f"Mów mi Python, mam {python_age} lat. Witaj w moim swiecie {name}. Jesteś {'starszy' if python_age < age else 'mlodszy'} ode mnie.")

imie = input("Podaj imię: ")
dlugosc = len(imie)
imie_odwrocone = ""
for x in range (dlugosc-1, -1, -1):
    imie_odwrocone = imie_odwrocone + imie[x]
print("Twoje imię od tyłu to: " + imie_odwrocone)

zdanie = input("Proszę wpisać zdanie:  ")
print("Dziękuję!")

podzielone = zdanie.split(" ")
dlugoscZdania = len(podzielone)
zdanieDobre = ""

for x in range (dlugoscZdania-1, -1, -1 ):
    zdanieDobre = zdanieDobre + " " + podzielone[x]
print(zdanieDobre)


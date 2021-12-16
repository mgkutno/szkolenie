ma = input("Miasto A: ")
mb = input("Miasto B: ")
dys = float(input("Dystans: "))
cena_paliwa = float(input("cena paliwa: "))
spalanie = float(input("Spalanie: "))
koszt = round((dys /100) * spalanie * cena_paliwa, 2)
print(f"Koszt przejazdu {ma}-{mb} to {koszt} PLN")



#słowniki
produkty = {
    "marchew": 1.23,
    "cebula": 0.56,
    "ziemniaki": 1.11,
}
for produkt, cena in produkty.items():
    print(f" - {produkt:20} - {cena:3.2f} PLN")

pr = input("co chcesz kupic? ")
ile = float(input("ile? "))
cena = ile * produkty[pr]

print("nalezność ", cena)
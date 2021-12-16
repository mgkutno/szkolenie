minimum = None
maxsimum = None
while True:
    polecenie = input("Podaj liczbe lub k by zakonczyc")
    if polecenie == "k": break
    if polecenie.isnumeric():
        liczba = int(polecenie)
    else:
        print("podaj liczbę")
    if minimum is None:
        minimum = liczba
        maksimum = liczba
    else:
        if liczba < minimum:
            minimum = liczba
        if liczba > maksimum:
            maksimum = liczba
print(f"MIn: {})

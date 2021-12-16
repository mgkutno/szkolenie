dane = []
for i in range(10):
    polecenie = input("Podaj liczbe lub k by zakonczyc")
    if polecenie == "k": break
    liczba = int(polecenie)
    dane.append(liczba)

print(sum(dane) / len(dane))

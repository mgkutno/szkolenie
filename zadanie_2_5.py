#napisy
napis = "Ala ma <kota>, a <kot> ma Alę"

licznik = 0
zliczaj = False
for litera in napis:
    if litera == "<":
        zliczaj=True  #ustawiamy flagę
    elif znak == ">":
        zliczaj=False
    elif zliczaj:
        licznik += 1
print(licznik)
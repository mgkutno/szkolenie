SAMOGŁOSKI = "aeiouy"
licznik =0
for znak in text.lower():
    if znak in SAMOGŁOSKI:
        licznik += 1
print(licznik)
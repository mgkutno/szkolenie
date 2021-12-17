#zapisać do pliku dane z listy, każdy element w nowej linii
#odczytać plik i wyświetlić ponumerowane wiersze
lista = ["xxx","yyy","zzz"]
with open("..\szkolenie\lista.txt", "w") as f:
    dane = "\n".join(lista)
    f.write(dane)

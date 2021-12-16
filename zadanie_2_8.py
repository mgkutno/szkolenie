lista = [9, 1, 6, 8, 4, 3, 2, 0]

for i in range(len(lista)):
    i_min = i
    for j in range(i+1, len(lista)):
        if lista[j] < lista[i_min]:
            i_min = j
    lista[i], lista[i_min] = lista[i_min], lista[i]
    print(lista)
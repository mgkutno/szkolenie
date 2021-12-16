def l_pierwsza(liczba):
    liczba = int(input("Podaj liczbę: "))
    for i in range(2, liczba):
        if liczba % 1 ==0:
            return False
    return True

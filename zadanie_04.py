# warunek if, elif, else
import datetime
rok = datetime.datetime.now()
cur_rok = datetime.now(year)
rok_urodzenia = int(input("Podaj rok urodzenia: "))
wiek = 2021 - cur_rok
if wiek >= 18:
    print("Jesteś pełnoletni")
else:
    print("Nie jesteś pełnoletni")

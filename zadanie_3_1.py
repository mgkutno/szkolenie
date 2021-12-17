def formatuj(*args, **kwargs):
    print(args)
    print(kwargs)
    napis = ""
    for n in args:
        napis += "\n"+n
    for klucz, text in kwargs.items():
        napis = napis.replace('$' + klucz, str(text))

formatuj(
    'koszt $cena PLN',
    'kwota $cena brutto. Podatek $podatek %,',
    cena = 10,
    podatek=23,
)
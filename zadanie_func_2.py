def wiecej_niz(text, prog):
    """zwraca zbior znaków występujących w text wiecej niż prog razy """
    result = set()
    for znak in set(text):
        if text.count(znak) > prog:
            result.add(znak)
    return result

assert wiecej_niz("", 4) == set()

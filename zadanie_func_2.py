def wiecej_niz(text, prog):
    result = set()
    for znak in set(text):
        if text.count(znak) > prog:
            result.add(znak)
    return result

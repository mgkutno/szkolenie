x = 7
p = 0
y = 0
while p < x:
    y = int(input(f"podaj temperaturę: {p+1}"))
    y += y
    print(y)
else:
    print("średnia", y/7)
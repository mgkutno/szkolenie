# while
x = 100
while x > 0:
    if x % 2 != 0:
        x -= 1
        continue
    print(x)
    x -=1
else:
    print("koniec")
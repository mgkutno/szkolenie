x = int(input("Pozycja x: "))
y = int(input("Pozycja Y: "))

if x >= 90 and y >= 90:
    print("jesteś w GP")
elif x <= 10 and y >= 90:
    print("jesteś w GL")
elif x <= 10 and y <= 10:
    print("jesteś w DL")
elif x >= 90 and y <= 10:
    print("jesteś w DP")
elif x <= 10 and y > 10 and y < 90:
    print("jesteś w L")
elif x > 10 and x < 90 and y > 90:
    print("jesteś w G")
elif x > 90 and y > 10 and y < 90:
    print("jesteś w P")
elif x > 10 and x < 90 and y  < 10:
    print("jesteś w D")
elif x > 10 and x < 90 and y > 10 and y < 90:
    print("Środek")
else:
    print("poza planszą")
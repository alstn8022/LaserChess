x1, y1, pos = [x for x in input().split(',')]
x2, y2 = [int(x) for x in input().split(',')]

x1 = int(x1)
y1 = int(y1)

x2 = int(x2)
y2 = int(y2)

if pos == "d":
    if y1 == 9:
        print("-1")
    elif y1 == y2:
        print("2")
    elif y1 > y2:
        if x1 == x2:
            print("3")
        else:
            print("2")
    else:
        if x1 == x2:
            print("0")
        else:
            print("1")

if pos == "u":
    if y1 == 0:
        print("-1")
    elif y1 == y2:
        print("2")
    elif y1 > y2:
        if x1 == x2:
            print("0")
        else:
            print("1")
    else:
        if x1 == x2:
            print("3")
        else:
            print("2")

if pos == "l":
    if x1 == 0:
        print("-1")
    elif y1 == y2:
        if x1 > x2:
            print("0")
        else:
            print("3")
    elif y1 > y2:
        if x1 > x2:
            print("1")
        else:
            print("2")
    else:
        if x1 > x2:
            print("1")
        else:
            print("2")

if pos == "r":
    if x1 == 9:
        print("-1")
    elif y1 == y2:
        if x1 > x2:
            print("3")
        else:
            print("0")
    elif y1 > y2:
        if x1 >= x2:
            print("2")
        else:
            print("1")
    else:
        if x1 >= x2:
            print("2")
        else:
            print("1")
            
x1, y1, alignedFrom = [x for x in input().split()]
x2, y2 = [int(x) for x in input().split()]

x1 = int(x1)
y1 = int(y1)
pos = input()
x2 = int(x2)
y2 = int(y2)

if pos == "d":
    if y1 > y2:
        if x1 > x2:
            print("2")
        elif x1 < x2:
            print("2")
        elif x1 == x2:
            print("3")
        else:
            print("-1")

if pos == "d":
    if y1 < y2:
        if x1 > x2:
            print("1")
        elif x1 < x2:
            print("1")
        elif x1 == x2:
            print("3")
        else:
            print("-1")

if pos == "d":
    if y1 == x2:
        if x1 > x2:
            print("2")
        elif x1 < x2:
            print("2")
        else:
            print("-1")

if pos == "u":
    if y1 > y2:
        if x1 > x2:
            print("1")
        elif x1 < x2:
            print("1")
        elif x1 == x2:
            print("3")
        else:
            print("-1")

if pos == "u":
    if y1 < y2:
        if x1 > x2:
            print("2")
        elif x1 < x2:
            print("2")
        elif x1 == x2:
            print("3")
        else:
            print("-1")

if pos == "u":
    if y1 == y2:
        if x1 > x2:
            print("2")
        elif x1 < x2:
            print("2")
        else:
            print("-1")

if pos == "l":
    if y1 > y2:
        if x1 > x2:
            print("1")
        elif x1 < x2:
            print("2")
        elif x1 == x2:
            print("2")
        else:
            print("-1")

if pos == "l":
    if y1 < y2:
        if x1 > x2:
            print("1")
        elif x1 < x2:
            print("2")
        elif x1 == x2:
            print("2")
        else:
            print("-1")

if pos == "l":
    if y1 == y2:
        if x1 > x2:
            print("3")
        elif x1 < x2:
            print("3")
        else:
            print("-1")
            
if pos == "r":
    if y1 > y2:
        if x1 > x2:
            print("2")
        elif x1 < x2:
            print("1")
        elif x1 == x2:
            print("2")
        else:
            print("-1")

if pos == "r":
    if y1 < y2:
        if x1 > x2:
            print("2")
        elif x1 < x2:
            print("1")
        elif x1 == x2:
            print("2")
        else:
            print("-1")

if pos == "r":
    if y1 == y2:
        if x1 > x2:
            print("3")
        elif x1 < x2:
            print("3")
        else:
            print("-1")

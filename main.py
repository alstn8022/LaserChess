x1 = int(input())
y1 = int(input())
pos = input()
x2 = int(input())
y2 = int(input())

if pos == "d" :
    if y1 > y2:
        if x1 > x2:
            print("")
        elif x1 < x2:
            print("")
    else: print("-1")
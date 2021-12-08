f = open("Day5.txt", "r")
lines = f.readlines()

N = 1000
M = 1000

zeros = [ [0] * N for _ in range(M)]

for vent in lines:
    vent = vent.replace(" -> ", ",")
    tmparr = vent.split(",")
    x1 = int(tmparr[0])
    y1 = int(tmparr[1])
    x2 = int(tmparr[2])
    y2 = int(tmparr[3])

    # vertical
    if (x1 == x2):
        print(vent)
        m = x1

        print(y1, y2)

        y_x = 0 
        y_y = 0
        if (y1 > y2):
            y_x = y1
            y_y = y2
        else: 
            y_y = y1
            y_x = y2
        for n in range (int(y_y), int(y_x) + 1):
            print(n)
            zeros[n][m] = zeros[n][m] + 1
    # horizontal
    elif (y1 == y2):
        n = y1
        x_x = 0
        x_y = 0
        if (x1 > x2):
            x_x = x1
            x_y = x2
        else: 
            x_y = x1
            x_x = x2

        print(vent)
        for m in range (int(x_y), int(x_x)+ 1):
            zeros[n][m] = zeros[n][m] + 1
    # diagonal 
    else:
        x_x = 0
        x_y = 0
        if (x1 > x2):
            x_x = x1
            x_y = x2
        else: 
            x_y = x1
            x_x = x2

        print(vent)
        for m in range (int(x_y), int(x_x)+ 1):
            slope = (y1 - y2) / (x1 - x2)
            b = (x1 * y2 - x2 * y1) / (x1 - x2)

            y = (slope * m) + b
            y = int(y)
            zeros[y][m] = zeros[y][m] + 1

t = 0
for arr in zeros:
    for el in arr:
        if (el > 1):
            t += 1
print(t)
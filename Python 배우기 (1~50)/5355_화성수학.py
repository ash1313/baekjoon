a = int(input(''))

for i in range(a):
    b = input('').split()
    res = float(b[0])
    for y in range(len(b)) : 
        if b[y] == '@' :
            res *= 3
        elif b[y] == '%' :
            res += 5
        elif b[y] == '#' :
            res -= 7
    print("%0.2f" % res)
a = int(input(''))
sum = 0
n = 0
for i in range(1, a+1):
    sum += i
    n += 1
    if (sum >a):
        n-=1
        break
print(n)
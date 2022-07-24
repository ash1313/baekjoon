a,b = map(int, input().split)

if b > 44:
    print(a, b-45)
elif a>=1 and b <= 44:
    print(a-1, b + 15)
else:
    print(23,b+15) 
H,M = map(int, input().split())
0 <= H <= 23, 0<= M <= 59
if H > 0:
    if M < 45:
        print(H-1,(M+60)-45)
    elif M >= 45:
        print(H,M-45)
if H == 0:
    if M >= 45:
        print(0,M-45)
    elif M < 45 :
        print(24-1,(M+60)-45)
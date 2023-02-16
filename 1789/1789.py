I=int(input())
C=0
T=0
for i in range(1,I+1):
    C+=1
    T+=i
    if T>I:
        print(C-1,end='')
        break
    elif T==I:
        print(C,end='')
        break
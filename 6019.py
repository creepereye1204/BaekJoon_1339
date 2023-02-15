IN_1=input()
N,L=IN_1.split(" ")
N=int(N)
L=int(L)

IN_2=input()
I=IN_2.split(" ")
I=list(map(int,I))

I.sort()
C=0
T=0


T=I[0]+L-1
C+=1
for i in range(1,len(I)):
    if T<I[i]:
        C+=1
        T = I[i] + L - 1
print(C,end='')



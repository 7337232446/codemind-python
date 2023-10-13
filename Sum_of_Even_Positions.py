n=int(input())
ls=list(map(int,input().split()))
s=0
for i in range(0,len(ls)):
    if i%2==0:
        s=s+ls[i]
print(s)
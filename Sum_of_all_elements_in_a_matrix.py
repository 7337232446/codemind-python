r,c=map(int,input().split())
mat=[]
for i in range(r):
    il=list(map(int,input().split()))
    mat.append(il)
s=0
for il in mat:
        for ev in il:
            s+=ev
print(s)
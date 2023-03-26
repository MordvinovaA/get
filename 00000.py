import copy
v=list(input().split())
if v==[]:
    print(0)
else:
    for i in range(len(v)):
        v[i]=list(map(int, str(v[i]).split('-')))
    i=-1
    q=2
    a=0
    while i<len(v):
 
        w=copy.copy(q)
        for q1 in range(1,w):
            i+=q1
            if i<len(v):
                if len(v[i])>1:
                    q+=1
        a+=1
    print(a)    
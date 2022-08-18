L,M,T,Y=map(int,input().split())
while True:
    d=""
    if Y<M:Y+=1;d="S"
    elif Y>M:Y-=1;d="N"
    if T<L:T+=1;d+="E"
    elif T>L:T-=1;d+="W"
    print(d)

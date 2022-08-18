L,R,B,W,d="LEFT","RIGHT","BLOCK","WAIT",{}
n,w,r,e,ep,c,el,l=map(int,input().split())
for i in range(l):f,p=input().split();d[int(f)]=int(p)
while True:
    a,b,c=input().split()
    a,b=int(a),int(b)
    if 0>=b>=w-1:print(B)
    try: 
        p=d[a]
        print(B if b<p and c==L or b>p and c==R else W)
    except: 
        print(B if b<ep and c==L or b>ep and c==R else W)

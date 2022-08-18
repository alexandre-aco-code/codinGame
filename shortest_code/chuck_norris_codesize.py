a,b,p="","",False
for c in input():a+="{0:07b}".format(ord(c))
if len(a)>=1:
    if a[0]=="0":b+="00 0"
    else:b+="0 0";p=True
for i in range(1,len(a)):
    if a[i]=="0" and p:b+=" 00 0";p=False
    elif a[i]=="1" and not p:b+=" 0 0";p=True
    else:b+="0"
print(b)

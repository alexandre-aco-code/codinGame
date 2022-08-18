bt,ut,p="","",False
for c in input():bt+="{0:07b}".format(ord(c))
if len(bt) >= 1:
    if bt[0]=="0":ut+="00 0"
    else:ut+="0 0";p=True
for i in range(1,len(bt)):
    if bt[i]=="0" and p:ut+=" 00 0";p=False
    elif bt[i]=="1" and not p:ut+=" 0 0";p=True
    else:ut+="0"
print(ut)

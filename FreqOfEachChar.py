s=input("Enter the string :")
f={}
for i in s:
    if i in f:
        f[i]+=1
    else:
        f[i]=1
print(f)




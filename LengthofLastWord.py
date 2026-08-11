s=input()
i=len(s)-1
count=0
for i in range(len(s)):
    if s[i]==" ":
        break
    i-=1
    count+=1
print(count)
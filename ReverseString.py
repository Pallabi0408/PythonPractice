str=input()
arr=list(str)#string to array
l=0
r=len(arr)-1
while l<r:
    arr[l],arr[r]=arr[r],arr[l]
    l+=1
    r-=1
str1="".join(arr)#arr to string
print(str1)
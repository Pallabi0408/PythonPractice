arr=list(map(int, input().split()))
j=0
for i in arr:
    if arr[i]!=0:
        arr[i],arr[j]=arr[j],arr[i]
print(arr)

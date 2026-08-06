arr=list(map(int, input().split()))
arr1=[]
for i in arr:
    if not arr1 or arr1[-1]!=i:#if arr1 is empty or last element of arr1 is not equal to i
        arr1.append(i)
print(arr1)
# Find the target element in an array
arr=list(map(int, input().split()))
target=int(input())
for i in range(len(arr)):
    if (arr[i]==target):
        print("Found at position",i)
        break
else:
    print("Not Found")

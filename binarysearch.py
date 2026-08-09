arr=list(map(int, input("Enter the elements for array").split()))
target=int(input("Enter the target element"))
left=0
right=len(arr)-1
while left<=right:
    mid=left+(right-left)//2
    if arr[mid]==target:
        print("The target is found at index",mid)
        break
    elif arr[mid]<target:
        left=mid+1
    else:
        right=mid-1
else:
    print("Target not found")
    
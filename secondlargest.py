arr=list(map(int, input("Enter the elements of array :").split()))
l=-float('inf')
sl=-float('inf')
for i in arr:
    if i>l:
        sl=l
        l=i
    elif i<l and i>sl:
        sl=i
print(l)
print(sl)

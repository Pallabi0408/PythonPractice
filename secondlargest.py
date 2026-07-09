arr=list(map(int, input("Enter the elements of array :").split()))
l=-float('inf')
sl=-float('inf')
for i in arr:
    if i>l:
        sl=l
        l=i
    elif i>sl and i!=l:
        sl=i
print(l)
print(sl)
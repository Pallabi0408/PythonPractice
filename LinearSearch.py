# Find the target element in an array
arr=list(map(int, input().split()))#take the input from user
target=int(input())
for i in range(len(arr)):#the loop will run from 0 to length of array-1
    if (arr[i]==target):#if the values matches with the target
        print("Found at position",i)
        break#here the iteration will be stopped
else:#if the for loop will not break, then the else will be executed
    print("Not Found")

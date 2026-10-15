#	Reverse a number without converting it to a string.	Easy
num=int(input("Enter a number :"))
rev=0
while(num!=0):
    d=num%10
    rev=rev*10+d
    num=num//10
print("The number is :",rev)

#For edge cases such as negative numbers
# num = int(input("Enter a number: "))

# temp = abs(num)
# rev = 0

# while temp != 0:
#     digit = temp % 10
#     rev = rev * 10 + digit
#     temp = temp // 10

# if num < 0:
#     rev = -rev

# print("Reversed number:", rev)
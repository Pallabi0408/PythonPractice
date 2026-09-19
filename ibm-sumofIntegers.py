# Given a positive integer N, find the sum of the digits of N.
num = int(input())
sum = 0

while num != 0:
    i = num % 10
    num = num // 10
    sum += i

print(sum)


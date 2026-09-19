# #Normal Approach
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# if a == 0 and b == 0:
#     print("HCF is undefined")

# elif a == 0:
#     print(abs(b))

# elif b == 0:
#     print(abs(a))

# else:
#     a_count = []
#     b_count = []

#     # Factors of a
#     for i in range(1, a + 1):
#         if a % i == 0:
#             a_count.append(i)

#     # Factors of b
#     for i in range(1, b + 1):
#         if b % i == 0:
#             b_count.append(i)

#     # Common factors
#     l = []

#     for i in a_count:
#         if i in b_count:
#             l.append(i)

#     # Greatest common factor
#     print(l[-1])

# # Optimal Approach(Euclidian Division Algorithm)
a=int(input())
b=int(input())
while b!=0:
    c=a%b
    a=b
    b=c
print(a)
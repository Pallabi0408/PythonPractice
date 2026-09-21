# with recursion
def Fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*Fact(n-1)
print(Fact(4))

#without recursion
m=int(input())
fact=1
for i in range(1,m+1):
    fact*=i
print(fact)


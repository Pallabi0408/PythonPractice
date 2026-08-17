s=input()
l=0
r=len(s)-1
while l<r:
    if s[l]!=s[r]:
        print("Not Palindrome")
        break
    l+=1
    r-=1
else:
    print("Palindrome")

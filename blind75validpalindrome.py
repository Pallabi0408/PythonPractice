s=input()
s=''.join(ch.lower() for ch in s if ch.isalnum())
l=0
r=len(s)-1
while l<=r:
    if s[l]!=s[r]:
        print("Not Palindrome")
    l+=1
    r-=1
else:
    print("Palindrome")
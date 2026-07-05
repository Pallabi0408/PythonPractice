# Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.
# Example 1:
# Input: nums = [1, 2, 3, 3]
# Output: true
# Example 2:
# Input: nums = [1, 2, 3, 4]
# Output: false

nums=list(map(int, input().split()))
f=set()#declare an empty set
for i in nums:
    if i in f:
        print("True")
        break
    f.add(i)
else:
    print("False")
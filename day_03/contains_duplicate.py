#Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

nums=[1,2,3,6,7,5]
for i in nums:
    if nums.count(i)>=2:
        print(True)
        break
else:
    print(False)

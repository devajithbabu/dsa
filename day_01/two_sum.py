#You are given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
nums=[3,1,3,2]
target=6
for n in range(0,len(nums)):
    a=target-nums[n]
    if a in nums and nums.index(a)!=n:
        print(n,nums.index(a))
        break
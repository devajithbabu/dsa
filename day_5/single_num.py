#Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
#You must implement a solution with a linear runtime complexity and use only constant extra space.
nums=[2,2,1,1,6,4,4,5,5]
result = 0

for i in nums:
    result ^= i

print(result)

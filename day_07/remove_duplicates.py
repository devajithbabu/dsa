#Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.
nums = [1, 2, 3, 3, 3, 3, 4, 4]

f = 0
l = 1

while l < len(nums):
    if nums[f] == nums[l]:
        l += 1

    else:
        f += 1
        nums[f] = nums[l]
        l += 1

k = f + 1

for i in range(k, len(nums)):
    nums[i] = "_"

print(nums)
print(k)
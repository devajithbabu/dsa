#Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

nums = [2, 3, 1, 2, 4, 3]
target = 7

l = 0
window_sum = 0
res = len(nums) + 1

for r in range(len(nums)):
    window_sum += nums[r]

    while window_sum >= target:
        res = min(res, r - l + 1)
        window_sum -= nums[l]
        l += 1

if res == len(nums) + 1:
    print(0)
else:
    print(res)


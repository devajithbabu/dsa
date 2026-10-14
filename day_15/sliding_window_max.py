#You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

nums = [1,3,-1,-3,5,3,6,7]

k = 3

l=0
r=k-1

res = []

for r in range(k-1,len(nums)):

    num = max(nums[l:r+1])

    res.append(num)

    l+=1

print(res)
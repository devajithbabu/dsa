#Given an integer array nums, find the subarray with the largest sum, and return its sum.
nums = [-2,1,-3,4,-1,2,1,-5,4]
i=0
cur_sum=0
sum=0
while i<len(nums):
    cur_sum+=nums[i]
    
    if cur_sum<=0:
        cur_sum=0
    
    if cur_sum>sum:
        sum=cur_sum
    i+=1 
print(sum)

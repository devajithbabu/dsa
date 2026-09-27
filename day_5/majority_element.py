nums=[2,2,1,1,1,2,2]
res=nums[0]
for i in nums:
    if nums.count(i)>nums.count(res):
        res=i
print(res)
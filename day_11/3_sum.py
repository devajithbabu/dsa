#Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

nums =[0,1,1]

res=[]

nums.sort()

num=nums[0]
for i in range(0,len(nums)-2):
    l=i+1
    r=len(nums)-1
    if num!=nums[i]:
        num=nums[i]
    
        while l<r:
            if nums[i]+nums[l]+nums[r]==0:
                res.append([nums[i],nums[l],nums[r]])
                l+=1
                r-=1
            elif nums[i]+nums[l]+nums[r]<0:
                l+=1
            elif nums[i]+nums[l]+nums[r]>0:
                r-=1
print(res)
#You are given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

nums = [2,0,2,1,1,0]

l=0
m=0
r=len(nums)-1

while m<=r:
    if nums[m]==2:
        nums[r],nums[m]=nums[m],nums[r]
        r-=1
    elif nums[m]==1:
        m+=1
    elif nums[m]==0:
        nums[m],nums[l]=nums[l],nums[m]
        m+=1
        l+=1
print(nums)
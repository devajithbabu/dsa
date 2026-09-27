#Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
nums=[0]
res=[]
n=0
for i in nums:
    if i==0:
        res.insert(-1,i)
    else:
        res.insert(n,i)
        n+=1
print(res)
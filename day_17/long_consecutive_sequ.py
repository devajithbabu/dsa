#Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
#You must write an algorithm that runs in O(n) time.

nums = [0,1,1,2]

nums=sorted(list(set(nums)))


i=0
thres=1
res=0

while i<len(nums)-1:

    f=nums[i]

    s=nums[i+1]

    if s-1==f:

        thres+=1

        if thres>res:

            res=thres

    else:

        thres=1

    i+=1

print(res)
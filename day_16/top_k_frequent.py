#Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

nums = [1,1,1,2,2,3]
k = 2

count={}

res=[]

lst=[[] for i in range(len(nums)+1)]

for i in nums:

    if i in count:

        count[i]+=1

    else:

        count[i]=1

for i,j in count.items():

    lst[j].append(i)

for i in range(len(lst)-1,0,-1):

    for j in lst[i]:

        res.append(j)

        if len(res)==2:
            break
    if len(res)==2:
                break    
            


print(res)
#Given the integer array fruits, return the maximum number of fruits you can pick.

fruits = [1,2,3,2,2]

l=0

lst = {}
tot=0
res=0

for i in fruits:

    if i not in lst:
        lst[i]=1
        tot+=1
    else:
        lst[i]+=1
        tot+=1

    while len(lst)>2:

        lst[fruits[l]]-=1
        tot-=1
        
        if lst[fruits[l]]==0:
            del lst[fruits[l]]
        l+=1

    res=max(res,tot)
print(res)




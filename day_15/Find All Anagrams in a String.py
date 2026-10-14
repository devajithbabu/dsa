#Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

s = "abab"
p = "ab"

res=[]

l=0
r=len(p)-1

for r in range(len(p)-1,len(s)):

    if sorted(s[l:r+1]) == sorted(p):

        res.append(l)

    l+=1
    

print(res)
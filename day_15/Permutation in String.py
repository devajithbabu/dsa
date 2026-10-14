#Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
#In other words, return true if one of s1's permutations is the substring of s2.

s1 = "ab"

s2 = "eidbaooo"

l=0

res=False

for r in range(len(s1)-1,len(s2)):

    if sorted(s2[l:r+1]) == sorted(s1):

        res=True

        break

    else:

        l+=1

print(res)
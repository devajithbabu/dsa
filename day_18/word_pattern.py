#Given a pattern and a string s, find if s follows the same pattern.


pattern = "abba"
s = "dog cat cat dog"
s=s.split()

d1={}
d2={}
n=0

for i in s:

    if (pattern[n] in d1 and d1[pattern[n]]!=i) or (i in d2 and d2[i]!=pattern[n]):

        print(False)
        break
    
    d1[pattern[n]]=i
    d2[i]=pattern[n]

    n+=1

else:

    print(True)
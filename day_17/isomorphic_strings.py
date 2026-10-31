#Given two strings s and t, determine if they are isomorphic.

 
# s = "egg"
 
# t = "add"

# s = "abca"
# t = "deed"

s = "abaa"
t = "xyyz"

s = "ayay"
t = "xyyx"
d1={}
d2={}
n=0
res=True

for i in range(len(s)):

    ch1,ch2=s[i],t[i]

    if (ch1 in d1 and d1[ch1]!=ch2) or (ch2 in d2 and d2[ch2]!=ch1):

        print(False)

        break
    d1[ch1]=ch2
    d2[ch2]=ch1
else:

    print(True)


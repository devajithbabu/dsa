#Given two strings s and t, return true if t is an anagram of s, and false otherwise.

s = "anagram"
t = "nagaram"

d={}

if len(s) != len(t):

    print(False)

else:

    for i in s:

        if i in d:

            d[i]+=1

        else:

            d[i]=1

    for i in t:

        if i not in d:

            print(False)

            break

        else:

            d[i]-=1

    else:

        if all(values==0 for values in d.values()):

            print(True)

        else:

            print(False)
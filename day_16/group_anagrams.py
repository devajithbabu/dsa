#Given an array of strings strs, group the anagrams together. You can return the answer in any order.

strs = ["eat","tea","tan","ate","nat","bat"]

d={}

for i in strs:

    key = "".join(sorted(i))

    if key not in d:

        d[key]=[i]

    else:

        d[key].append(i)

print(list(d.values()))



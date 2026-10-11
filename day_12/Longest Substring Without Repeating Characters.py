#Given a string s, find the length of the longest substring without duplicate characters.

s = "pwwkew"
# res=[]
# length=len(res)
# for i in s:
#     if i not in res:
#         res.append(i)
#     else:
#         if len(res)>length:
#             length=len(res)
#         res.clear()
#         res.append(i)
# print(length)

s = "p w w k k e w"
d = "0 1 2 3 4 5 6"

l = 0
r = 0
chars = set()
length = 0

while r < len(s):
    if s[r] not in chars:
        chars.add(s[r])
        length = max(length, r - l + 1)
        r += 1
    else:
        chars.remove(s[l])
        l += 1

print(length)

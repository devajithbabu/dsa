#You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.
#Return the length of the longest substring containing the same letter you can get after performing the above operations.

s = "ABCDE"
k = 2

freqs = {}
res = 0
i = 0

for j in range(len(s)):
    letterJ = s[j]

    if letterJ not in freqs:
        freqs[letterJ] = 1
    else:
        freqs[letterJ] += 1

    maxFreq = max(freqs.values())
    curLen = j - i + 1

    if curLen - maxFreq > k:
        freqs[s[i]] -= 1
        i += 1
        curLen = j - i + 1

    res = max(res, curLen)

print(res)
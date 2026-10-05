#A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

s="A man, a plan, a canal: Panama"

wrd="".join([i.lower() for i in s if i.isalpha()])

l=0
r=len(wrd)-1
while 1<r:
    if wrd[l]!=wrd[r]:
        print(False)
        break

    else:
        l+=1
        r-=1

else:
    print(True)
    

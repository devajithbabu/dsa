#Write a function that reverses a string. The input string is given as an array of characters s.
#You must do this by modifying the input array in-place with O(1) extra memory.


def rev():
    s=list(input("enter word"))
    l=0
    r=len(s)-1
    while l<r:
        s[r],s[l]=s[l],s[r]
        r-=1
        l+=1
    print(s)
rev()
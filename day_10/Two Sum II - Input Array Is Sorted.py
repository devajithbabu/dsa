#You are given a 1-indexed array of integers numbers that is already sorted in non-decreasing order.
#Find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
#Return the indices of the two numbers index1 and index2 as an integer array [index1, index2] of length 2.

numbers=[1,2,3,4,5]
t=5
l=0
r=len(numbers)-1
while l<r:
    if numbers[r]+numbers[l] == t:
        print([l+1,r+1])
        break
    elif numbers[l]+numbers[r] < t:
        l+=1
    elif numbers[l]+numbers[r] > t:
        r-=1
        
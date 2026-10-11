#You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
#Find two lines that together with the x-axis form a container, such that the container contains the most water.
#Return the maximum amount of water a container can store.

height = [3, 20, 25, 2, 3]

l=0
r=len(height)-1
sol=0
while(l<r):
    res = (r-l)*min(height[l],height[r])
    if res>sol:
        sol=res
    if height[l]<height[r]:
        l+=1
    else:
        r-=1
print(sol)


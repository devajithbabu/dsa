#You are given a large integer represented as an integer array digits, where each digits[i] is 
# the ith digit of the integer. The digits are ordered from most significant to 
# least significant in left-to-right order. The large integer does not contain any leading 0's.

#Increment the large integer by one and return the resulting array of digits.

digits=[9]
num=digits[-1]
num+=1
digits.pop()
for i in str(num):
    digits.append(int(i))
print(digits)

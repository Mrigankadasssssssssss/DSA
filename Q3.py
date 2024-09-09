'''
Question 3. A list of integers nums (1<=len(num)<=10^5) representing an array
of numbers. Return the maximum sum of any contiguous subarray in the given
array.
Example:
Input : -2 1 -3 4 -1 2 1 -5 4
Output: 6

Input : 3 -1 2 5 -6 3
Output: 9
'''

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
cs = 0
ms = 0

for i in arr:
    cs += i
    if cs<0:
        cs=0
    ms = max(cs,ms)

print(ms)

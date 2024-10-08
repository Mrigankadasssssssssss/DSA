'''
Question 2. Given an array of random numbers, Push all the zero’s of a given an
array to the end of the array. All non-zero elements should come in front and
Order of all non-zero elements should be same.
Input Format: Given an array of random numbers.
Output Format: Move all zeros to end of array and keeping all non-zero
element in same position.

Input 1: 1 2 0 4 3 0 5 0
Output 1: 1 2 4 3 5 0 0 0

Input 1: 1 2 0 0 0 3 6
Output 1: 1 2 3 6 0 0 0
'''

a = [1, 2, 0, 0, 0,3,6]

zeros = []
for i in range(len(a)-1,-1,-1):
    if a[i] == 0:
        zeros.append(a.pop(i))

print(a+zeros)
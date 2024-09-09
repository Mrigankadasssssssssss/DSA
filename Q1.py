'''
Ques 1. Given an array of N size, Print the Next Greater Element of every
element.
The Next Great Element for an element x is the first greater element on the
right side of x in the array. Elements for which no greater element exist,
consider the next greater element as -1
Input Format: Given array of N size with space separated integers.
Output: Array of size N with next greater element.
Input 1: 4 5 2 25
Output 1: 5 25 25 -1
Input 2: 5 7 1 7 6 0
Output 2: 7 -1 7 -1 -1 -1
'''
arr = [4, 5, 2 ,25]
ans = [-1]*len(arr)
stack = [arr[-1]] # stack = [25(top)]
for i in range(len(arr)-2,-1,-1):
    
    while stack and arr[i]>=stack[-1]:
        stack.pop()
    if stack: 
        ans[i] = stack[-1]
    stack.append(arr[i])

print(ans)


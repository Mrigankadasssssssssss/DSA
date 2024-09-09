'''
Question 4: Nearest Integer
Int nearestInteger(int num, int m)
The function accepts two positive ‘num’ and ‘m’ as its argument, Implement
the following function to find the nearest integer to num.
1) Number is divisible by m.
2) Number is nearest to ‘num’ (Have the least distance from num)
Note: If there are two numbers with the least distance from num, then return
the larger num.
Input 1: Num= 67
M = 8
Output 1: 64

Input 2: Num=26
M=3
Output 2: 27
'''

def nearestInt(num,m):
    lower = num//m * m
    upper = lower + m
    if (num-lower) < (upper-num):
        return lower
    else:
        return upper

print(nearestInt(67,8))
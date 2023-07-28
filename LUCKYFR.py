'''
Karan likes the number 4 very much.

Impressed by the power of this number, Karan has begun to look for occurrences of four anywhere. He has a list of T integers, for each of them he wants to calculate the number of occurrences of the digit 4 in the decimal representation. He is too busy now, so please help him.

Input Format
The first line of input consists of a single integer T, denoting the number of integers in Karan's list.

Then, there are T lines, each of them contain a single integer from the list.

Output Format
Output T lines. Each of these lines should contain the number of occurrences of the digit 4 in the respective integer from Karan's list.

Constraints
1 ≤ T ≤ 10^5
(Subtask 1): 0 ≤ Numbers from the list ≤ 9 - 33 points.
(Subtask 2): 0 ≤ Numbers from the list ≤ 109 - 67 points.
Sample 1:
Input
Output
5
447474
228
6664
40
81
4
0
1
1
0
'''

#logic
t = int(input())
nums= list()

for i in range(0, t):
    num = int(input())
    nums.append(num)
    
def check_four(num):
    count = 0
    while (num > 0):
        if num%10==4:
            count += 1
        num = int(num/10)
    return count
    
for i in range(0, t):
    print(check_four(nums[i]))

#pythonic
for i in range(int(input())):
    print([*input()].count('4'))
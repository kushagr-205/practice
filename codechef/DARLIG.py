'''
Problem
Tonmoy has a special torch. The torch has 
4
4 levels numbered 
1
1 to 
4
4 and 
2
2 states (
On
On and 
Off
Off). Levels 
1
,
2
,
1,2, and 
3
3 correspond to the 
On
On state while level 
4
4 corresponds to the 
Off
Off state.

The levels of the torch can be changed as:

Level 
1
1 changes to level 
2
2.
Level 
2
2 changes to level 
3
3.
Level 
3
3 changes to level 
4
4.
Level 
4
4 changes to level 
1
1.
Given the initial state as 
�
K and the number of changes made in the levels as 
�
N, find the final state of the torch. If the final state cannot be determined, print 
Ambiguous
Ambiguous instead.

Input Format
First line will contain 
�
T, the number of test cases. Then the test cases follow.
Each test case contains of a single line of input, two integers 
�
,
�
N,K - the number of changes made in the levels and initial state of the torch. Here, 
�
=
0
K=0 denotes 
Off
Off state while 
�
=
1
K=1 denotes 
On
On state.
Output Format
For each test case, output in a single line, the final state of the torch, i.e. 
On
On or 
Off
Off. If the final state cannot be determined, print 
Ambiguous
Ambiguous instead.

You may print each character of the string in uppercase or lowercase (for example, the strings 
On
On, 
ON
ON, 
on
on and 
oN
oN will all be treated as identical).

Constraints
1
≤
�
≤
1
0
5
1≤T≤10 
5
 
0
≤
�
≤
1
0
9
0≤N≤10 
9
 
0
≤
�
≤
1
0≤K≤1
Sample 1:
Input
Output
3
4 0
0 1
3 1
Off
On
Ambiguous
Explanation:
Test Case 
1
1: Initially, the torch is in 
Off
Off state. Since only level 
4
4 corresponds to the 
Off
Off state, the torch is at level 
4
4 initially. After 
4
4 changes, the final level would be 
4
4. Level 
4
4 corresponds to the 
Off
Off state. Hence, finally the torch is 
Off
Off.

Test Case 
2
2: Initially, the torch is in 
On
On state. After 
0
0 changes, the torch remains in the 
On
On state.

Test Case 
3
3: Initially, the torch is in 
On
On state. This can correspond to any of the first 
3
3 levels. Thus, we cannot determine the final level after 
3
3 changes. Hence, the final state is 
Ambiguous
Ambiguous.
'''

for i in range(int(input())):
    n, k = map(int,input().split())
    if k == 1:
        if n%4 == 0:
            print("On")
        else:
            print("Ambiguous")
    
    else:
        if n%4 == 0:
            print("Off")
        else:
            print("On")
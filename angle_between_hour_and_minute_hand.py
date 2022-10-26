'''
Calculate the angle between hour hand and minute hand.

There can be two angles between hands, we need to print minimum of two.
Also, we need to print floor of final result angle.
For example, if the final angle is 10.61, we need to print 10.

Input:
The first line of input contains a single integer T denoting the number of test
cases. Then T test cases follow. Each test case consists of one line conatining
two space separated numbers h and m where h is hour and m is minute.

Output:
Coresponding to each test case, print the angle b/w hour and min hand in a
separate line.

Constraints:
1 ≤ T ≤ 100
1 ≤ h ≤ 12
1 ≤ m ≤ 60
'''

#Solution:

def angle(h, t):
    if(t == 60 or t == 0):
        t = 0
    ans = abs((h*30 + t*0.5) - (t*6))
    if(ans > 180):
        ans = 360 - ans
    return int(ans)

def main():
    t = int(input())
    res = []
    for i in range(t):
        h, t = input().split()
        h, t = float(h), float(t)
        res.append(angle(h, t))

    for i in res:
        print(i)


main()

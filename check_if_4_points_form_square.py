'''
Given coordinates of four points in a plane, find if the four points form a
square or not.

Input:
The first line of input contains an integer T denoting the number of test cases.
Then T test cases follow. The first line of each test case contains 4 space
separated integer points a , b , c , d

Output:
For each test case print 1 if the four points form a square else print 0.
Remember to output the answer of each test case in a new line.

Constraints:
1 <= T <= 200
1 <= a,b,c,d <= 100
'''

# Solution:

def check_square(points):
    points_dict = {}
    for i in points:
        if i not in points_dict:
            points_dict[i] = 1
        else:
            points_dict[i] += 1

    for key in points_dict:
        if points_dict[key] != 4:
            return 0

    return 1

def main():
    t = int(input())
    res = []
    for i in range(t):
        points = list(map(int, input().rstrip().split()))
        res.append(check_square(points))

    for i in res:
        print(i)

main()

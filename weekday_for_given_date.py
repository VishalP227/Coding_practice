'''
Write a program that calculates the day of the week for any particular date in
the past or future.

Input:
The first line of input contains a single integer T denoting the number of t
est cases. Then T test cases follow. Each test case consist of one line.
The first line of each test case consists of an integer d,m and y, d is day,
m is month and y is the year.

Output:
Print day of given date.

Constraints:
1 ≤ T ≤ 100
1990 ≤ Y ≤ 2100
'''

#Solution:

month_dict = {
        1: 0,
        2: 3,
        3: 3,
        4: 6,
        5: 1,
        6: 4,
        7: 6,
        8: 2,
        9: 5,
        10: 0,
        11: 3,
        12: 5
    }

century_dict = {
    1: 4,
    2: 2,
    3: 0,
    0: 6
}

day_dict = {
    0: "Sunday",
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday"
}

def check_leap_year(year):
    if(year % 4) == 0:
        if(year % 100) == 0:
            if(year % 400) == 0:
                ans = 1
            else:
                ans = 0
        else:
            ans = 1
    else:
        ans = 0

    return ans


def weekday(dd,mm,yyyy):

    yy = yyyy%100
    year_code = int((yy + (yy/4))%7)
    month_code = month_dict[mm]
    century = int(yyyy / 100)
    century_code = century_dict[century%4]
    day_code = year_code + month_code + century_code + dd

    if(check_leap_year(yyyy) and (mm is 1 or mm is 2)):
        day_code = day_code - 1

    day_code = (day_code % 7)

    return day_dict[day_code]



def main():
    t = int(input())
    res = []
    for i in range(t):
        dd,mm,yyyy = input().split(" ")
        dd,mm,yyyy = int(dd), int(mm), int(yyyy)
        res.append(weekday(dd,mm,yyyy))

    for i in res:
        print(i)

main()

'''
Given a value N. The task is to find how many numbers less than or equal to N
have numbers of divisors exactly equal to 3.

Input:
The first line contains integer T, denoting number of test cases. Then T test
cases follow. The only line of each test case contains an integer N.

Output :
For each testcase, in a new line, print the answer of each test case.

Constraints :
1 <= T <= 10^3
1 <= N <= 10^12
'''

# Solution:

# Program 2 from bhatabhi554 Geeks for Geeks

import math
a=[0]*1000001
def SieveOfEratosthenes(n):
    # Create a boolean array "prime[0..n]" and initialize
    #  all entries it as true. A value in prime[i] will
    # finally be false if i is Not a prime, else true.

    prime = [True for i in range(n+1)]
    p = 2

    while (p * p <= n):

        # If prime[p] is not changed, then it is a prime
        if (prime[p] == True):

            # Update all multiples of p
            for i in range(p * p, n+1, p):
                prime[i] = False

        p += 1

    # Print all prime numbers
    for p in range(2, n):
        if prime[p]:
            a[p]=1+a[p-1]
        else:
            a[p]=a[p-1]


# driver program

if __name__=='__main__':

    n = 1000001

    #print "Following are the prime numbers smaller",
    #print "than or equal to", n

    SieveOfEratosthenes(n)
    for _ in range(int(input())):
        print(a[int(math.sqrt(int(input())))])

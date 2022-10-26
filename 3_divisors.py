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
# Program 1
import math

def SieveOfEratosthenes(n):

    primes = [True for i in range(n+1)]
    primes[0] = primes[1] = False
    p = 2
    while(p * p <= n):
        if(primes[p] == True):
            for i in range(p * p, n+1, p):
                primes[i] = False;

        p += 1

    return primes

def main():
    n = 1000001
    c = 0
    primes = SieveOfEratosthenes(n);
    t = int(input())
    for i in range(t):
        num = int(math.sqrt(int(input())))
        c = primes[:num+1].count(1)
        print(c)

main()

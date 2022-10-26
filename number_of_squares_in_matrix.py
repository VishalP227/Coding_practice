from math import factorial as fact

def countSquares(n, m):
    sq_sum = 0
    for i in range(min(n,m)):
        sq_sum += (n-i)*(m-i)
    return sq_sum

def main():
    t = int(input())
    sq_sum = 0
    for i in range(t):
        n, m = input().rstrip().split()
        n, m = int(n), int(m)
        print(countSquares(n,m))

main()

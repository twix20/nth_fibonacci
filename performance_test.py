from timeit import default_timer as timer
from fibonacci import fibonacci
import sys

sys.setrecursionlimit(1500)

def fib_nth(n):
    """
        Python implementation of nth fib
    """
    F = [[1,1],[1,0]]
    if n == 0:
        return 0

    power(F, n-1)
    return F[0][0]

def multiply(F, M):
    x =  F[0][0]*M[0][0] + F[0][1]*M[1][0]
    y =  F[0][0]*M[0][1] + F[0][1]*M[1][1]
    z =  F[1][0]*M[0][0] + F[1][1]*M[1][0]
    w =  F[1][0]*M[0][1] + F[1][1]*M[1][1]

    F[0][0] = x
    F[0][1] = y
    F[1][0] = z
    F[1][1] = w

def power(F, n):
    if n == 0 or n == 1:
        return

    M = [[1,1],[1,0]]

    power(F, int(n/2))
    multiply(F, F)

    if n%2 != 0:
        multiply(F, M)

def stress(fib, n, times):
    start = timer()

    for _ in range(times):
        fib(n)

    end = timer()

    return end - start


N = 45
TIMES = 900000
result_format = '{0}: {1}s'


print(fibonacci.nth(N))
print(fib_nth(N))

print('Nth fibbonaci performance tester')
print('Find {0}th fib {1} times'.format(N, TIMES))
print(result_format.format('C++', stress(fibonacci.nth, N, TIMES)))
print(result_format.format('Python', stress(fib_nth, N, TIMES)))
from timeit import default_timer as timer
import sys

from fibonacci import fibonacci as cpp_fib
import python_fib as py_fib

def benchmark(fib, n, times):
    """
        Stresses fib function with N number x times
    """
    start = timer()

    for _ in range(times):
        fib(n)

    end = timer()

    return end - start


if __name__ == "__main__":
    assert len(sys.argv) == 3, 'Example usage python {0} 50 1000, 50th fib number 1000 times'.format(sys.argv[0])

    N = int(sys.argv[1])
    TIMES = int(sys.argv[2])

    assert cpp_fib.nth(N) == py_fib.nth(N), 'C++ and Python result is not the same'

    result_format = '{0}: {1}s'
    print('Nth fibbonaci performance tester')
    print('Find {0}th fib {1} times'.format(N, TIMES))
    print(result_format.format('C++', benchmark(cpp_fib.nth, N, TIMES)))
    print(result_format.format('Python', benchmark(py_fib.nth, N, TIMES)))

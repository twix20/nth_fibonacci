#include <stdio.h>
#include <Python.h>

typedef unsigned long long ulong_t;

void multiply(ulong_t F[2][2], ulong_t M[2][2])
{
  ulong_t x =  F[0][0]*M[0][0] + F[0][1]*M[1][0];
  ulong_t y =  F[0][0]*M[0][1] + F[0][1]*M[1][1];
  ulong_t z =  F[1][0]*M[0][0] + F[1][1]*M[1][0];
  ulong_t w =  F[1][0]*M[0][1] + F[1][1]*M[1][1];
 
  F[0][0] = x;
  F[0][1] = y;
  F[1][0] = z;
  F[1][1] = w;
}
 
void power(ulong_t F[2][2], ulong_t n)
{
  if( n == 0 || n == 1)
      return;
  ulong_t M[2][2] = {{1,1},{1,0}};
 
  power(F, n/2);
  multiply(F, F);
 
  if (n%2 != 0)
     multiply(F, M);
}

/* function that returns nth Fibonacci number */
ulong_t fib_nth(ulong_t n)
{
  ulong_t F[2][2] = {{1,1},{1,0}};
  if (n == 0)
    return 0;
  power(F, n-1);
  return F[0][0];
}
 
static PyObject * nth_wrapper(PyObject * self, PyObject * args)
{
    ulong_t input;
    ulong_t result;
    PyObject * ret;

    // parse arguments
    if (!PyArg_ParseTuple(args, "K", &input)) {
        return NULL;
    }

    // run the actual function
    result = fib_nth(input);

    // build the resulting ulong_t ulong_to a Python object.
    ret = PyLong_FromUnsignedLongLong(result);
    return ret;
}

static PyMethodDef FibonacciMethods[] = {
  { "nth", nth_wrapper, METH_VARARGS, "Calculate Nth fib number" },
  { NULL, NULL, 0, NULL }
};

PyModuleDef fibonacci_mod = {
	PyModuleDef_HEAD_INIT,
	"fibonacci",
	"This is fibonacci extension",
	-1,
	FibonacciMethods,
	NULL,
	NULL,
	NULL,
	NULL
};

PyMODINIT_FUNC PyInit_fibonacci(void) {
	return PyModule_Create(&fibonacci_mod);
}
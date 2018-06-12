from distutils.core import setup, Extension

# the c++ extension module
extension_mod = Extension("fibonacci", ["fibonacci.cpp"])

setup(
    name = "fibonacci",
    description = 'C++ fib extension test',
    ext_modules=[extension_mod])
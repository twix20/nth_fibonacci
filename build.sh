#clean previous build
rm -rf build fibonacci_pkg dist *.egg-info __pycache__
rm -f *.pyd *.spec

if [[ $* == --clean ]]; then
    exit 0
fi

#build extension
python setup_ext.py build_ext --inplace

#create module
mkdir --parents ./fibonacci_pkg
mv fibonacci.*.pyd ./fibonacci_pkg
touch ./fibonacci_pkg/__init__.py

#dist wheel
python setup_dist.py sdist bdist_wheel
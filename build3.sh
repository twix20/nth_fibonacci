#clean previous build
rm -rf build fibonacci dist *.egg-info __pycache__
rm -f *.pyd *.spec

if [[ $* == --clean ]]; then
    exit 0
fi

#build extension
python3 setup_ext.py build_ext --inplace

#create module
mkdir --parents ./fibonacci
mv fibonacci.*.pyd fibonacci.*.so ./fibonacci
touch ./fibonacci/__init__.py

#dist wheel
python3 setup.py sdist bdist_wheel

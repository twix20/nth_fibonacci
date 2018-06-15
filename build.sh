#clean previous build
rm -rf build fibonacci dist *.egg-info __pycache__
rm -f *.pyd *.spec

if [[ $* == --clean ]]; then
    exit 0
fi

#build extension
python setup_ext.py build_ext --inplace

#create module
mkdir --parents ./fibonacci
mv fibonacci.*.pyd ./fibonacci
touch ./fibonacci/__init__.py

#dist wheel
python setup.py sdist bdist_wheel

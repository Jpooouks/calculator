from setuptools import setup

with open("README.md","r") as fh:
    long_description = fh.read()

setup(
    name='tc-ds-2023-calculator',
    version='0.1.0',
    description='Contains Calculator Class\
    used for performing basic arithmetic operations',
    py_modules=['calculator'],
    package_dir={'': 'src'},
    long_description=long_description,
    long_description_content_type="text/markdown",
    test_suite="tests",
    
)
    

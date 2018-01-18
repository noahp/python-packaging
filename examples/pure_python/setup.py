"""
Example setup.py for building distutils wheels.
"""
from setuptools import setup
setup(
    name='pure_python',
    version='0.0.1',
    description='Prints hello!',
    author='Noah Pendleton',
    author_email='noahp@users.noreply.github.com',
    url='https://github.com/noahp/python-packaging/examples/pure_python',

    packages=['pure_python'],

    # These scripts are installed to your python environment and should be available on PATH after
    # installing this package. Note that they should be executable (`chmod +x`) and contain an
    # appropriate shebang, such as `#!/usr/bin/env` python for python scripts
    scripts=['pure_python_script'],

    # For scripts, this corrects shebang replacement, from:
    #  https://github.com/pybuilder/pybuilder/issues/168
    options={'build_scripts': {'executable': '/usr/bin/env python'}},
)

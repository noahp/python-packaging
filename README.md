# 🐍 python-packaging
Cheatsheet on python packaging.

References:
- Wheel reference https://packaging.python.org/tutorials/distributing-packages
- setuptools docs https://setuptools.readthedocs.io/en/latest/setuptools.html
- Setupscript information https://docs.python.org/2/distutils/setupscript.html
- Excellent guide on PyPi https://hynek.me/articles/sharing-your-labor-of-love-pypi-quick-and-dirty

For a REALLY quick setup for a new package, you can use [pyscaffold](https://github.com/blue-yonder/pyscaffold):
```bash
pip install pyscaffold  # for python 3
pip install pyscaffold==2.5  # for python 2.x
putup new-package  # initializes a git repo in a new folder `new-package` with a skeleton package
```

# Use
Copy the example `setup.py` and modify for your use.

Run the following commands from the package directory to produce the `.whl` package file.

```bash
# Install wheel utils if you don't already have them
pip install wheel

# To build a plain python (or if there are native extensions, a platform wheel):
python setup.py bdist_wheel
```

The `.whl` file generated can be installed with pip locally, and also uploaded to a python package repository.

I recommend testing in a clean virtualenv to make sure any scripts or dependencies are handled properly.

Note that the naming scheme for the `.whl` file should not be modified, it's processed by setuptools when fetching and installing the package.

# setup.py
The informative parameter values (version, author, url, etc.) are available from `pip show` after installing the wheel.
```python
"""
Example setup.py for building distutils wheels.
"""
from setuptools import setup, Extension
setup(
    name='some-package',
    version='0.0.1',
    description='Describe the package',
    author='Your name',
    author_email='username@users.noreply.github.com',
    url='https://github.com/username/some-repo',

    # If your module is set up as a package, using the standard layout:
    #  some_package
    #  ├── __init__.py
    #  └── some_package.py
    packages=['some_package'],
    # Many modern packages use this structure; the python3 version of pyscaffold follows this:
    #  ├── setup.py
    #  ├── src
    #  │   └── some_package
    #  │       ├── __init__.py
    #  │       └── some_module.py
    # Then using `find_packages` to include pacakges under src/
    from setuptools import find_packages
    packages=find_packages(where='src'),

    # Individual modules you want to be available for `import` after installing the package
    # In this example, some_package.py would be in the same directory as this `setup.py` script
    py_modules=['some_package'],

    # These scripts are installed to your python environment and should be available on PATH after
    # installing this package. Note that they should be executable (`chmod +x`) and contain an
    # appropriate shebang, such as `#!/usr/bin/env` python for python scripts
    scripts=['util.py'],

    # For scripts, this corrects shebang replacement, from:
    #  https://github.com/pybuilder/pybuilder/issues/168
    options={'build_scripts': {'executable': '/usr/bin/env python'}},

    # Dependencies listed here
    install_requires=['pyyaml==1.2.3'],

    # A simple example for native c python extensions- specify the sources and compile args here
    # Note that this native extension will produce a platform-specfic wheel, see
    #  https://packaging.python.org/tutorials/distributing-packages/#platform-wheels and
    #  https://docs.python.org/2/distutils/setupscript.html#describing-extension-modules
    ext_modules=[
        Extension('foo',
                  sources=[
                      'foo/foo.c',
                  ],

                  include_dirs=['foo/inc', ],

                  # Example compile/link args; usually unnecessary for simple extensions
                  extra_compile_args=[
                      '-I./extra', '-fPIC', '--std=gnu99', '-Wall', '-Werror', '-g'],
                  extra_link_args=['-L./extra', '-static', '-lfoo']
                  )
    ]
)
```

# Single source of version
This snippet can be added to a `setup.py` file. It grabs a `__version__` string from the specified file, and uses it when producing the package file.

Clumsy but it works! Using scm (git semver tags) instead would require the package to retrieve its version number from `pkg_resources` after installation.

```python
import os
import re
def get_version():
    """One of the practical options for single source of versioning. See:
    https://packaging.python.org/guides/single-sourcing-package-version/"""
    package_name = os.path.join(os.path.dirname(__file__), 'some-package.py')
    with open(package_name, 'r') as package:
        find_version = re.compile(r'^__version__ = [\'\"]([^\'\"]*)[\'\"]')
        for line in package.readlines():
            m = find_version.search(line)
            if m:
                return m.group(1)
    raise UserWarning('Error, unable to locate version string')
...
setup(
    ...
    version=get_version(),
    ...
)
```
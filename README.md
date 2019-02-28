# 🐍 python-packaging
Cheatsheet on python packaging.

References:

- A detailed example `setup.py`: https://github.com/pypa/sampleproject/blob/master/setup.py
- Wheel reference: https://packaging.python.org/tutorials/distributing-packages
- Setuptools docs: https://setuptools.readthedocs.io/en/latest/setuptools.html
- Setupscript information: https://docs.python.org/2/distutils/setupscript.html
- Excellent guide on PyPi: https://hynek.me/articles/sharing-your-labor-of-love-pypi-quick-and-dirty

For a REALLY quick setup for a new package, you can use
[pyscaffold](https://github.com/blue-yonder/pyscaffold):

```bash
# for python 3
pip install pyscaffold
# for python 2.x
pip install pyscaffold==2.5
# initializes a git repo + skeleton package in a new folder 'new-package'
putup new-package
```

# Use
1. Copy the example `setup.py` and modify for your use.

2. Run the following commands from the package directory to produce the `.whl`
   package file.

```bash
# Install wheel utils if you don't already have them
pip install wheel

# To build a plain python (or if there are native extensions, a platform wheel):
python setup.py bdist_wheel
```

The `.whl` file generated can be installed with pip locally, and also uploaded
to a python package repository.

I recommend testing in a clean virtualenv (or use
[tox](https://tox.readthedocs.io/en/latest/) ✨ ) to make sure any scripts or
dependencies are handled properly.

# setup.py
The informative parameter values (version, author, url, etc.) are available from
`pip show` after installing the wheel.

```python
"""
Example setup.py for building distutils wheels.
"""
from setuptools import setup, Extension

# If your package has a README.md
import io
with io.open("README.md", encoding="utf-8") as readme:
    LONG_DESCRIPTION = readme.read()

setup(
    name='some-package',
    # semver guidelines recommend 0.1.0 for initial development version; 1.0.0
    # reserved for the first public api release
    version='0.1.0',
    description='Describe the package',
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    author='Your name',
    author_email='username@users.noreply.github.com',
    url='https://github.com/username/some-repo',

    # Option project urls are visible from the pypi landing page
    project_urls={
        "Code": "https://github.com/username/some-repo",
        "Issue tracker": "https://github.com/username/some-repo/issues",
    },
    # If your module is set up as a package, using the standard layout:
    #  some_package
    #  ├── __init__.py
    #  └── some_package.py
    # Manually select packages to include
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
    # Alternate form:
    # package=find_packages(exclude=('tests',)),

    # Individual modules you want to be available for `import` after installing the package
    # In this example, some_package.py would be in the same directory as this `setup.py` script
    py_modules=['some_package'],

    # A preferrable way to install console scripts, using the entry point directive, selecting a
    # python function to be installed to a particular console_script (here "my-script").
    # More information and examples see
    #  https://python-packaging.readthedocs.io/en/latest/command-line-scripts.html#the-console-scripts-entry-point
    #  https://amir.rachum.com/blog/2017/07/28/python-entry-points/
    entry_points={
        "console_scripts": [
            "my-script=some_package:main",
        ],
    },

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
    ],

    # Trove classifiers; see full list here:
    # https://pypi.org/pypi?%3Aaction=list_classifiers
    # These fill many pieces of the metadata when you upload to pypi.org.
    # For example, specifying python versions as below example enables badges-
    # https://shields.io/category/platform-support "PyPI - Python Version"
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.6",
        "Operating System :: OS Independent",
    ]
)
```

# Single source of version
This snippet can be added to a `setup.py` file. It grabs a `__version__` string
from the specified file, and uses it when producing the package file.

Clumsy but it works! Using scm (git semver tags) instead would require the
package to retrieve its version number from `pkg_resources` after installation.

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

"""
Example setup.py for building distutils wheels.
"""
from setuptools import setup, Extension
setup(
    name='platform_wheel',
    version='0.0.1',
    description='Example platform wheel',
    author='Noah Pendleton',
    author_email='noahp@users.noreply.github.com',
    url='https://github.com/noahp/python-packaging/examples/platform_wheel',

    py_modules=['platform_wheel'],

    # These scripts are installed to your python environment and should be available on PATH after
    # installing this package. Note that they should be executable (`chmod +x`) and contain an
    # appropriate shebang, such as `#!/usr/bin/env` python for python scripts
    scripts=['platform_wheel_script'],

    # For scripts, this corrects shebang replacement, from:
    #  https://github.com/pybuilder/pybuilder/issues/168
    options={'build_scripts': {'executable': '/usr/bin/env python'}},

    ext_modules=[
        # This exports the `platform_wheel_extension` native c module
        Extension('platform_wheel_extension',
                  sources=['platform_wheel_extension.c',],
                  extra_compile_args=['--std=gnu99', '-Wall', '-Werror'],
                 )
    ]
)

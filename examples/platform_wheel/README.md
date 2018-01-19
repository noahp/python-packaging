# examples/platform_wheel
A simple example with a native c extension. When running `python setup.py bdist_wheel` the output will be a platform-specific wheel.

This also shows how a script `platform_wheel_script` can be distributed with the package.

To try it out, run `pip install .` (`--upgrade` to overwrite) in this directory. You should then be able to try out the package:

```bash
# use the c extension directly
➜ python -c "import platform_wheel_extension; print platform_wheel_extension.sqrtf(4.0)"
2.0

# use the python wrapper of the c extension
➜ python -c "import platform_wheel; print platform_wheel.use_extension(9.0)"
3.0

# use the installed script
➜ platform_wheel_script 2.0
1.41421353817
```

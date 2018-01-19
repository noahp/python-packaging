# examples/pure_python
A really simple example using a python package (`__init__.py`) module.

This also shows how a script `pure_python_script` can be distributed with the package.

To try it out, run `pip install .` in this directory. You should then be able to try out the package:

```bash
➜ python -c "import pure_python; pure_python.print_hello()"
hello!
➜ pure_python_script
hello!
```

# examples/pure_python
A really simple example with a bare python module. This is about as simple as it gets!

This also shows how a script `pure_python_script` can be distributed with the package.

To try it out, run `pip install .` in this directory. You should then be able to try out the package:

```bash
➜ python -c "import pure_python; pure_python.print_hello()"
hello!
➜ pure_python_script
hello!
```

// Simple example c extension
#include <Python.h>
#include <math.h>

static PyObject *
platform_wheel_extension_sqrtf(PyObject *self, PyObject *args)
{
    const float input;

    if (!PyArg_ParseTuple(args, "f", &input)) {
        return NULL;
    }
    float result = sqrtf(input);
    return Py_BuildValue("f", result);
}

// Table of initialization information for all exported functions
static PyMethodDef ExtensionFunctions[] = {
    {
        .ml_name = "sqrtf",
        .ml_meth = platform_wheel_extension_sqrtf,
        .ml_flags = METH_VARARGS,
        .ml_doc = "Square root"
     },
    {NULL, NULL, 0, NULL} /* Sentinel */
};

// Init function is mandatory- it loads the exported functions
PyMODINIT_FUNC
initplatform_wheel_extension(void)
{
    PyObject *m = Py_InitModule("platform_wheel_extension", ExtensionFunctions);
    if (m == NULL) {
        return;
    }
}

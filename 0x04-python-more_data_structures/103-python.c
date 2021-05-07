#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p)
{
	PyObject* repr = PyObject_Repr(p);
	PyObject* str = PyUnicode_AsEncodedString(repr, "utf-8", "~E~");
	const char *bytes = PyBytes_AS_STRING(str);

	printf("REPR: %s\n", bytes);

	Py_XDECREF(repr);
	Py_XDECREF(str);
}

void print_python_bytes(PyObject *p)
{
	PyObject* repr = PyObject_Repr(p);
	PyObject* str = PyUnicode_AsEncodedString(repr, "utf-8", "~E~");
	const char *bytes = PyBytes_AS_STRING(str);

	printf("REPR: %s\n", bytes);

	Py_XDECREF(repr);
	Py_XDECREF(str);
}

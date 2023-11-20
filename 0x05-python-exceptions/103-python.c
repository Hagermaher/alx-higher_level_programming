#include <Python.h>
#include <stdio.h>
/**
 * print_python_float - gives data
 * @p: PyObject
 */
void print_python_float(PyObject *p)
{
	double val = 0;
	char *str = NULL;

	fflush(stdout);
	printf("[.] float object info\n");

	if (!PyFloat_CheckExact(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	val = ((PyFloatObject *)p)->ob_fval;
	str = PyOS_double_to_string(value, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", str);
}
/**
 * print_python_bytes - gives data
 * @p: PyObject
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t si = 0, w = 0;
	char *str = NULL;

	fflush(stdout);
	printf("[.] bytes object info\n");
	if (!PyBytes_CheckExact(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	si = PyBytes_Size(p);
	printf("  size: %zd\n", si);
	string = (assert(PyBytes_Check(p)), (((PyBytesObject *)(p))->ob_sval));
	printf("  trying string: %s\n", str);
	printf("  first %zd bytes:", si < 10 ? si + 1 : 10);
	while (w < si + 1 && w < 10)
	{
		printf(" %02hhx", str[w]);
		w++;
	}
	printf("\n");
}
/**
 * print_python_list - gives data
 * @p: PyObject
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t si = 0;
	PyObject *it;
	int w = 0;

	fflush(stdout);
	printf("[*] Python list info\n");
	if (PyList_CheckExact(p))
	{
		si = PyList_GET_SIZE(p);
		printf("[*] Size of the Python List = %zd\n", si);
		printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
		while (w < si)
		{
			it = PyList_GET_ITEM(p, w);
			printf("Element %d: %s\n", w, it->ob_type->tp_name);
			if (PyBytes_Check(it))
				print_python_bytes(it);
			else if (PyFloat_Check(it))
				print_python_float(it);
			w++;
		}
	}
	else
		printf("  [ERROR] Invalid List Object\n");
}

#include <Python.h>
#include <stdio.h>

/**
 * print_python_bytes - prints python bytes object
 * @p: the PyObject
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i, n;
	char *str;

	fflush(stdin);
	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_Size(p);
	printf("  size: %zd\n", size);

	str = PyBytes_AS_STRING(p);
	printf("  trying string: %s\n", str);
	if (size < 10)
		n = size + 1;
	else
		n = 10;
	printf("  first %zd bytes:", n);
	for (i = 0; i < n; i++)
		printf(" %02x", (unsigned int)str[i]);
	printf("\n");
}

/**
 * print_python_float = prints a float info
 * @p: the PyObject
 */
void print_python_float(PyObject *p)
{
	fflush(stdout);
	printf("[.] float object info\n");
	if (!PyFloat_Check(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	printf("  value: %f\n", PyFloat_AsDouble(p));
}

/**
 * print_python_list - prints python list info
 * @p: the PyObject
 */
void print_python_list(PyObject *p)
{
	PyListObject *list;
	PyObject *item;
	Py_ssize_t i, size;

	fflush(stdout);
	printf("[*] Python list info\n");
	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}
	list = (PyListObject *)p;
	size = PyList_GET_SIZE(p);

	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", list->allocated);

	for (i = 0; i < size; i++)
	{
		item = PyList_GET_ITEM(p, i);

		if (PyBytes_Check(item))
		{
			printf("Element %zd: bytes\n", i);
			print_python_bytes(item);
		}
		else if (PyFloat_Check(item))
		{
			printf("Element %zd: float\n", i);
			print_python_float(item);
		}
		else
		{
			printf("Element %zd: %s\n", i, item->ob_type->tp_name);
		}
	}
}

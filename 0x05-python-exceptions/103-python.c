#include <Python.h>
#include <stdio.h>

void print_python_bytes(PyObject *);
void print_python_float(PyObject *);

/**
 * print_python_list - prints python list
 * @p: the list
 */
void print_python_list(PyObject *p)
{
	PyObject *item;
	Py_ssize_t size;
	Py_ssize_t allocated;
	Py_ssize_t i;

	setbuf(stdout, NULL);

	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	size = PyList_GET_SIZE(p);
	allocated = ((PyListObject *)p)->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", allocated);

	for (i = 0; i < size; i++)
	{
		item = PyList_GET_ITEM(p, i);
		printf("Element %zd: %s\n", i, item->ob_type->tp_name);

		if (PyBytes_Check(item))
			print_python_bytes(item);
		else if (PyFloat_Check(item))
			print_python_float(item);
	}
}

/**
 * print_python_bytes - print spython byte
 * @p: the object
 */
void print_python_bytes(PyObject *p)
{
	char *string;
	Py_ssize_t size;

	setbuf(stdout, NULL);

	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_Size(p);
	string = PyBytes_AsString(p);

	printf("[.] bytes object info\n");
	printf("  size: %zd\n", size);
	printf("  trying string: %s\n", string);

	printf("  first %zu bytes:", (size >= 10) ? 10 : size + 1);

	for (Py_ssize_t i = 0; i < size && i < 10; i++)
	{
		printf(" %02x", (unsigned char)string[i]);
	}

	printf("\n");
}

/**
 * print_python_float - printf float info
 * @p: the object
 */
void print_python_float(PyObject *p)
{
	double value;

	setbuf(stdout, NULL);
	if (!PyFloat_Check(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	value = PyFloat_AS_DOUBLE(p);

	printf("[.] float object info\n");
	printf("  value: %.15g\n", value);
}

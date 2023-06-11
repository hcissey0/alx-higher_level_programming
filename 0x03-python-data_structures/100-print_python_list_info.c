#include <Python.h>
#include <stdio.h>

/**
7 * print_python_list_info - prints a python list info
 * p: the PyObject
 * Return: void
 */
void print_python_list_info(PyObject *p)
{
	long int size, i;
	PyListObject *list;
	PyObject *item;

	if (!PyList_Check(p))
		return;
	list = (PyListObject *)p;
	size = PyList_Size(p);
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);
	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}

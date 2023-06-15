#include <Python.h>

/**
 * print_python_bytes - prints python byte info
 * @p: the pyobject
 * Return: void
 */
void print_python_bytes(PyObject *p)
{
	long int size;
	int i;
	char *try_str = NULL;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	size = PyBytes_Size(p);
	try_str = PyBytes_AsString(p);
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", try_str);
	if (size < 10)
		printf("  first %ld bytes:", size + 1);
	else
		printf("  first 10 bytes:");
	for (i = 0; i <= size && i < 10; i++)
		printf(" %02hhx", try_str[i]);
	printf("\n");
}

/**
 * print_python_list - prints python list info
 * @p: pyobject
 * Return: void
 */
void print_python_list(PyObject *p)
{
	long int size, i;
	const char *t;
	PyListObject *l = (PyListObject *)p;

	if (!PyList_Check(p))
		return;

	size = PyList_Size(p);
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", l->allocated);
	for (i = 0; i < size; i++)
	{
		t = (l->ob_item[i])->ob_type->tp_name;
		printf("Element %ld: %s\n", i, t);
		if (!strcmp(t, "bytes"))
			print_python_bytes(l->ob_item[i]);
	}
}

#include <stdio.h>
#include <Python.h>

/**
 * print_python_string - prints a python string
 * @p: the python string
 */
void print_python_string(PyObject *p)
{
	PyUnicodeObject *unicode;
	const char *type;

	printf("[.] string object info\n");

	if (!PyUnicode_Check(p))
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}
	unicode = (PyUnicodeObject *)p;

	if(PyUnicode_IS_COMPACT_ASCII(unicode))
		type = "compact ascii";
	else if (PyUnicode_IS_COMPACT(unicode))
		type = "compact unicode object";
	else
		type = "unicode object";
	printf("  type: %s\n", type);
	printf("  length: %zd\n", PyUnicode_GET_LENGTH(unicode));
	printf("  value: %ls\n", PyUnicode_AS_UNICODE(unicode));
}


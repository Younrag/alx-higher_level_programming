#include <stdio.h>
#include <stdlib.h>
#include <Python.h>
#include <floatobject.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
 * print_python_list - Basic info Python lists.
 * @p: A PyObject list object.
 */
void print_python_list(PyObject *p)
{
        long int size = PyList_Size(p);
        int i;
        PyListObject *list = (PyListObject *)p;
        const char *type;

        printf("[*] Python list info\n");
        printf("[*] Size of the Python List = %li\n", size);
        printf("[*] Allocated = %li\n", list->allocated);
        for (i = 0; i < size; i++)
        {
                type = (list->ob_item[i])->ob_type->tp_name;
		printf("Element %i: %s\n", i, type);
                if (!strcmp(type, "bytes"))
                        print_python_bytes(list->ob_item[i]);
		else if (!strcmp(type, "float"))
			print_python_float(list->ob_item[i]);
	}
}

/**
 * print_python_bytes - Basic info Python byte objects.
 * @p: A PyObject byte object.
 */
void print_python_bytes(PyObject *p)
{
	long int size;
	int i;
	char *trying_str = NULL;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	PyBytes_AsStringAndSize(p, &trying_str, &size);

	printf("  size: %li\n", size);
	printf("  trying string: %s\n", trying_str);
	if (size < 10)
		printf("  first %li bytes:", size + 1);
	else
		printf("  first 10 bytes:");
	for (i = 0; i <= size && i < 10; i++)
		printf(" %02hhx", trying_str[i]);
	printf("\n");
}

/**
 * print_python_float - Basic info Python float objects.
 * @p: A PyObject float object.
 */
void print_python_float(PyObject *p)
{
	char *buffer = NULL;

	PyFloatObject *float_obj = (PyFloatObject *)p;

	fflush(stdout);

	printf("[.] float object info\n");
	if (strcmp(p->ob_type->tp_name, "float") != 0)
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	buffer = PyOS_double_to_string(float_obj->ob_fval, 'r', 0,
			Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", buffer);
	PyMem_Free(buffer);
}


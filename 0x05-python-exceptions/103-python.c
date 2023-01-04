#include <stdio.h>
#include <stdlib.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);


/**
 * print_python_list - print some basic info about Python lists
 * @p: holds some infomation about the python object file
 */
void print_python_list(PyObject *p)
{
	(void)p;
	printf("[*] Python list info\n");
	printf("    ERROR] Invalid List Object\n");
}

/**    
 * print_python_bytes - print some basic info about Python bytes
 * @p: holds some infomation about the python object file
 */                                                                          
void print_python_bytes(PyObject *p)
{
	(void)p;
	printf("[.] bytes object info\n");
	printf("    [ERROR] Invalid Bytes Object\n");
}

/**
* print_python_float - print some basic info about Python floats
* @p: holds some info about the python object file
*/
void print_python_float(PyObject *p)
{
	(void)p;
	printf("[.] float object info\n");
	printf("    [ERROR] Invalid Float Object\n");
}

# 0x07. Python - Test-driven development
## UnitTests
## Resources
<a href="https://docs.python.org/3.4/library/doctest.html">doctest — Test interactive Python examples </a>
<a href="https://pymotw.com/3/doctest/">doctest – Testing through documentation</a>
<a href="https://mattermost.com/blog/testing-python-understanding-doctest-and-unittest/">Interactive and Non-interactive tests</a>

___NB: All test files are in the test Directory___

## Files --- Description

#### 0-add_integer.py --- Write a function that adds 2 integers.
*  def add_integer(a, b=98):
* a and b must be integers or floats, otherwise raise a TypeError exception with the message a must be an integer or b must be an integer
* a and b must be first casted to integers if they are float
* Returns an integer: the addition of a and b

#### 2-matrix_divided.py --- Write a function that divides all elements of a matrix.
* Prototype: def matrix_divided(matrix, div):
* matrix must be a list of lists of integers or floats, otherwise raise a TypeError exception with the message matrix must be a matrix (list of lists) of integers/floats
* Each row of the matrix must be of the same size, otherwise raise a TypeError exception with the message Each row of the matrix must have the same size
* div must be a number (integer or float), otherwise raise a TypeError exception with the message div must be a number
* div can’t be equal to 0, otherwise raise a ZeroDivisionError exception with the message division by zero
* All elements of the matrix should be divided by div, rounded to 2 decimal places
* Returns a new matrix

#### 3-say_my_name.py --- Write a function that prints My name is <first name> <last name>
* Prototype: def say_my_name(first_name, last_name=""):
* first_name and last_name must be strings otherwise, raise a TypeError exception with the message first_name must be a string or last_name must be a string

#### 4-print_square.py --- Write a function that prints a square with the character #.
* Prototype: def print_square(size):
* size is the size length of the square
* size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
* if size is less than 0, raise a ValueError exception with the message size must be >= 0
* if size is a float and is less than 0, raise a TypeError exception with the message size must be an integer

#### 5-text_indentation.py --- Write a function that prints a text with 2 new lines after each of these characters: ., ? and :
* Prototype: def text_indentation(text):
* text must be a string, otherwise raise a TypeError exception with the message text must be a string
* There should be no space at the beginning or at the end of each printed line

#### tests/6-max_integer_test.py --- In this task, you will write unittests for the function def max_integer(list=[]):.
* You have to use the unittest module
* Your test file should be python files (extension: .py)
* Your test file should be executed by using this command: python3 -m unittest tests.6-max_integer_test
* All tests you make must be passable by the function below


# Python - Test-driven development

This project focuses on Test-Driven Development (TDD) in Python. Each task involves writing tests first, then implementing the function.

## Requirements

- All files interpreted on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- Code uses pycodestyle (version 2.7.\*)
- All test files are in the `tests/` folder

## Tasks

### 0. Integers addition
`0-add_integer.py` - Function that adds 2 integers, with type checking.

### 1. Divide a matrix
`2-matrix_divided.py` - Function that divides all elements of a matrix by a divisor.

### 2. Say my name
`3-say_my_name.py` - Function that prints "My name is <first name> <last name>".

### 3. Print square
`4-print_square.py` - Function that prints a square using the # character.

### 4. Text indentation
`5-text_indentation.py` - Function that prints text with 2 new lines after each '.', '?', and ':'.

### 5. Max integer - Unittest
`tests/6-max_integer_test.py` - Unittests for the `max_integer` function.

## Testing

Run doctest tests:
```bash
python3 -m doctest -v ./tests/*.txt
```

Run unittest tests:
```bash
python3 -m unittest tests.6-max_integer_test
```

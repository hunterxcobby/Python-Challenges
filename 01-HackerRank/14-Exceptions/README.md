# Exception Handling

Exceptions are errors detected during execution. Here are examples of common exceptions:

## ZeroDivisionError

This error is raised when the second argument of a division or modulo operation is zero.

```python
a = '1'
b = '0'
try:
    result = int(a) / int(b)
except ZeroDivisionError as e:
    print(f"Error Code: {e}")
```

Output:

```
Error Code: integer division or modulo by zero
```

## ValueError

This error is raised when a built-in operation or function receives an argument that has the right type but an inappropriate value.

```python
a = '1'
b = '#'
try:
    result = int(a) / int(b)
except ValueError as e:
    print(f"Error Code: {e}")
```

Output:

```
Error Code: invalid literal for int() with base 10: '#'
```

## Task

You are given two values, `a` and `b`. Perform integer division and print the result.

**Input Format:**

The first line contains `t`, the number of test cases.
The next `t` lines each contain the space-separated values of `a` and `b`.

**Constraints:**

- `t` is the number of test cases.
- `0 < a < 10^4`
- `0 < b < 10^4`

**Output Format:**

Print the value of the integer division.

In the case of `ZeroDivisionError` or `ValueError`, print the error code.

**Sample Input:**

```
3
1 0
2 $
3 1
```

**Sample Output:**

```
Error Code: integer division or modulo by zero
Error Code: invalid literal for int() with base 10: '$'
3
```

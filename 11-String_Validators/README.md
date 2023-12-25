# String Validation

Python provides built-in string validation methods to check various properties of a string. The following methods are commonly used:

- **`str.isalnum():`** Checks if all characters in the string are alphanumeric.

    ```python
    print('ab123'.isalnum())  # True
    print('ab123#'.isalnum())  # False
    ```

- **`str.isalpha():`** Checks if all characters in the string are alphabetical.

    ```python
    print('abcD'.isalpha())  # True
    print('abcd1'.isalpha())  # False
    ```

- **`str.isdigit():`** Checks if all characters in the string are digits.

    ```python
    print('1234'.isdigit())  # True
    print('123edsd'.isdigit())  # False
    ```

- **`str.islower():`** Checks if all characters in the string are lowercase.

    ```python
    print('abcd123#'.islower())  # True
    print('Abcd123#'.islower())  # False
    ```

- **`str.isupper():`** Checks if all characters in the string are uppercase.

    ```python
    print('ABCD123#'.isupper())  # True
    print('Abcd123#'.isupper())  # False
    ```

## Task

Given a string `s`, your task is to determine if it contains alphanumeric characters, alphabetical characters, digits, lowercase, and uppercase characters.

## Input Format

A single line containing a string `s`.

## Constraints

## Output Format

Print the following lines:

1. True if `s` has any alphanumeric characters, otherwise False.
2. True if `s` has any alphabetical characters, otherwise False.
3. True if `s` has any digits, otherwise False.
4. True if `s` has any lowercase characters, otherwise False.
5. True if `s` has any uppercase characters, otherwise False.

## Sample Input

```
qA2
```

## Sample Output

```
True
True
True
True
True
```

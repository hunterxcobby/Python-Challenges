# Logo Design

In Python, string alignment methods `ljust()`, `center()`, and `rjust()` can be used to align text left, center, and right, respectively.

- **`ljust(width, fillchar):`** Returns a left-aligned string of length `width` filled with `fillchar`.

    ```python
    width = 20
    print('HackerRank'.ljust(width, '-'))
    # Output: HackerRank----------
    ```

- **`center(width, fillchar):`** Returns a centered string of length `width` filled with `fillchar`.

    ```python
    width = 20
    print('HackerRank'.center(width, '-'))
    # Output: -----HackerRank-----
    ```

- **`rjust(width, fillchar):`** Returns a right-aligned string of length `width` filled with `fillchar`.

    ```python
    width = 20
    print('HackerRank'.rjust(width, '-'))
    # Output: ----------HackerRank
    ```

## Task

You are given a partial code for generating the HackerRank Logo with variable thickness. Your task is to replace the blanks (`______`) with `rjust`, `ljust`, or `center` methods.

## Input Format

A single line containing the thickness value for the logo.

## Constraints

The thickness must be an odd number.

## Output Format

Output the desired logo.

## Sample Input

```
5
```

## Sample Output

```
    H    
   HHH   
  HHHHH  
 HHHHHHH 
HHHHHHHHH
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHHHHHHHHHHHHHHHHHHHHHH   
  HHHHHHHHHHHHHHHHHHHHHHHHH   
  HHHHHHHHHHHHHHHHHHHHHHHHH   
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
                    HHHHHHHHH 
                     HHHHHHH  
                      HHHHH   
                       HHH    
                        H
```


---

# List Comprehensions Challenge

This Python challenge explores the concept of list comprehensions. Given three integers, `x`, `y`, and `z`, representing the dimensions of a cuboid, and an integer `n`, the task is to print a list of all possible coordinates on a 3D grid where the sum of coordinates is not equal to `n`.

## Example

### Input

```
1
1
1
2
```

### Output

```
[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
```

## Explanation

For the given input, each variable `x`, `y`, and `z` will have values of 0 or 1. All permutations of lists are generated in the form `[i, j, k]`. Arrays that sum to `n` are then removed, leaving only the valid permutations.

## Constraints

- The output list is printed in lexicographic increasing order.
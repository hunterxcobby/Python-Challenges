# Runner-Up Score Finder

Given the participants' score sheet for the University Sports Day, this program helps you find the runner-up score. It takes the number of participants and their scores as input, then prints the runner-up score.

## Input Format

- The first line contains an integer, `n`, representing the number of participants.
- The second line contains `n` space-separated integers, representing the scores of the participants.

## Constraints

- 2 <= n <= 10^5
- -100 <= score <= 100

## Output Format

Print the runner-up score.

## Sample Input

```
5
2 3 6 6 5
```

## Sample Output

```
5
```

## Explanation

The given list of scores is `[2, 3, 6, 6, 5]`. The maximum score is `6`, and the second maximum is `5`. Therefore, the runner-up score is `5`.
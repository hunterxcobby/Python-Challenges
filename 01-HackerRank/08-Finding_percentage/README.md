## Student Average Calculator

The provided Python code calculates and prints the average marks for a specific student based on the input data. Here's a guide on using the program:

### Input Format
1. The first line contains an integer, `n`, representing the number of students' records.
2. The next `n` lines contain the names and marks obtained by each student, separated by spaces.
3. The final line contains `query_name`, the name of the student for whom the average is to be calculated.

### Output Format
The program prints the average of the marks obtained by the specified student, correct to 2 decimal places.

### Sample Input
#### Input 1
```
3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika
```
#### Output 1
```
56.00
```

#### Input 2
```
2
Harsh 25 26.5 28
Anurag 26 28 30
Harsh
```
#### Output 2
```
26.50
```

### Usage
1. Input the number of students' records (`n`).
2. Enter the names and marks for each student.
3. Specify the `query_name` for the student whose average marks you want to find.

### Note
Ensure the marks are separated by spaces, and the query name matches the exact name in the records. The program calculates the average with precision up to 2 decimal places.
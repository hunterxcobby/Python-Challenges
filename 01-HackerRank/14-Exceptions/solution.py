# Enter your code here. Read input from STDIN. Print output to STDOUT

def perform_integer_division(a, b):
    try:
        result = int(a) // int(b)
        print(result)
    except (ZeroDivisionError, ValueError) as e:
        print(f"Error Code: {e}")

if __name__ == "__main__":
    t = int(input(""))
    for _ in range(t):
        a, b = input().split()
        perform_integer_division(a, b)

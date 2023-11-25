# Enter your code here. Read input from STDIN. Print output to STDOUT
def is_subset(set_a, set_b):
    # Check if every element in set_a is also in set_b
    return all(element in set_b for element in set_a)

def main():
    # Read the number of test cases
    t = int(input())

    for _ in range(t):
        # Read sets A and B
        _ = input()  # Disregard the size of set A (not needed for Python)
        set_a = set(map(int, input().split()))
        _ = input()  # Disregard the size of set B (not needed for Python)
        set_b = set(map(int, input().split()))

        # Check if set A is a subset of set B and print the result
        result = is_subset(set_a, set_b)
        print(result)

if __name__ == "__main__":
    main()

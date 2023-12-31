def print_rangoli(size):
    # Create a list of alphabets
    alphabets = 'abcdefghijklmnopqrstuvwxyz'

    # Loop through the range of size in reverse order
    for i in range(size - 1, 0, -1):
        # Print the left side of the rangoli
        print('-'.join(alphabets[size - 1:i:-1] + alphabets[i:size]).center(size * 4 - 3, '-'))

    # Loop through the range of size
    for i in range(size):
        # Print the right side of the rangoli
        print('-'.join(alphabets[size - 1:i:-1] + alphabets[i:size]).center(size * 4 - 3, '-'))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

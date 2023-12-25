if __name__ == '__main__':
    s = input()

    # Check if the string contains alphanumeric characters
    print(any(c.isalnum() for c in s))

    # Check if the string contains alphabetical characters
    print(any(c.isalpha() for c in s))

    # Check if the string contains digits
    print(any(c.isdigit() for c in s))

    # Check if the string contains lowercase characters
    print(any(c.islower() for c in s))

    # Check if the string contains uppercase characters
    print(any(c.isupper() for c in s))

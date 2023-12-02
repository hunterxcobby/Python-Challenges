if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    # Generate list comprehensions for all possible coordinates
coordinates = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1)]

# Filter coordinates where the sum is not equal to n
result = [coord for coord in coordinates if sum(coord) != n]

# Print the final result
print(result)

if __name__ == '__main__':
    # Read input
    n = int(input())
    arr = list(map(int, input().split()))

    # Find unique scores
    unique_scores = set(arr)

    # Remove the maximum score
    unique_scores.remove(max(unique_scores))

    # Find the second maximum score
    runner_up_score = max(unique_scores)

    # Print the result
    print(runner_up_score)

def pattern_3(n=5):
    """Square with diagonal X of stars."""
    for i in range(n):
        for j in range(n):
            if i == j or j == n - i - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

pattern_3()

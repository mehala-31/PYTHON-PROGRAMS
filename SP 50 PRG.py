def pattern_10(n=5):
    for i in range(n):
        if i % 2 == 0:
            print("* " * n)
        else:
            print("- " * n)

pattern_10()

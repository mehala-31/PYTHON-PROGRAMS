def pattern_6(n=5):
    for i in range(n):
        if i == 0 or i == n - 1:
            print("* " * n)
        else:
            print("*" + " " * (n - 2) + "*")

pattern_6()

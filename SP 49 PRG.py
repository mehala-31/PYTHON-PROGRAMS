def pattern_9(n=5):
    num = 1
    for i in range(n):
        row = ""
        for j in range(n):
            row += str(num % 10) + " "
            num += 1
        print(row)

pattern_9()

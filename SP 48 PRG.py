def pattern_8(n=5):
    for i in range(n):
        row = ""
        for j in range(n):
            if i == 0 or j == 0:
                row += "* "
            else:
                row += "  "
        print(row)

pattern_8()

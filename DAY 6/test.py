rows = 7
columns = rows - 2
pattern = ""
k = -1
# loop through the pattern rows.
for i in range(rows):
    # loop through the pattern columns.
    for j in range(columns):
        # print '*' at the beginning and end of the row in the first and last rows.
        if (i == 0 or i == rows - 1) and (j == 0 or j == columns - 1):
            pattern += "*"
        # print the x pattern in the rest of the rows.
        elif i != 0 and i != rows - 1 and (j == k or j == columns - 1 - k):
            pattern += "*"
        # print space where there should be no '*'
        else:
            pattern += " "
    k += 1
    pattern += "\n"
print(pattern)

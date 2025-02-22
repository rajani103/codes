n = 1
for i in range(1, n + 1):  # Loop for rows
    for j in range(n - i):  # Print spaces for alignment
        print(" ", end="")
    for k in range(i):  # Print stars
        print("* ", end="")
    print()  # Move to the next line

# Input the size of the snowflake
n = int(input("Enter the size of the snowflake:"))
# Create the array - initialize with a space
a = []
for i in range(n):
    a.append([' '] * n)
# Loop through the array by column
for i in range(n):
# left to right diagonal
	a[i][i] = '*'
# middle row
	a[n // 2][i] = '*'
# middle column
	a[i][n // 2] = '*'
# right to left diagonal	
	a[i][n - i - 1] = '*'
# print the snowflake
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=' ')
    print()
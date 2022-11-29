m = int(input("enter number of rows:"))
matrix = []
for c in range(m):
    row = input().split()
    matrix.append(row)

for row in range(len(matrix)):
    for col in range(len(matrix(row))):
        print(matrix[row][col], end=" ")
        



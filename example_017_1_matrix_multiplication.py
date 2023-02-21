# Input two matrices of size n x m
matrix_A = [[1, 2, 3],
            [1, 2, 3],
            [1, 2, 3]]

matrix_B = [[1, 0, 0],
            [0, 1, 0],
            [0, 0, 1]]

matrix_C = [[0 for x in range(len(matrix_A))] for y in range(len(matrix_B[0]))]

# explicit for loops
for i in range(len(matrix_A)):
	for j in range(len(matrix_B[0])):
		for k in range(len(matrix_B)):

			# resulted matrix
			matrix_C[i][j] += matrix_A[i][k] * matrix_B[k][j]

print(matrix_C)

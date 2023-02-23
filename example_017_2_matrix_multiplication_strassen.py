import numpy as np

def split(matrix):
	'''
	This is a simple split function to divde the input matrices
	'''
	row, col = matrix.shape
	row2, col2 = row//2, col//2
	return matrix[:row2, :col2], matrix[:row2, col2:], matrix[row2:, :col2], matrix[row2:, col2:]

def strassen(x, y):
	'''
	Computes matrix product by divide and conquer approach, recursively.
	Input: n x n numpy array matrices x and y
	Output: n x n matrix, product of x and y
	'''

	# Base case when size of matrices is 1x1
	if len(x) == 1:
		return x * y

	# Splitting the matrices into quadrants. This will be done recursively
	# until the base case is reached.
	a, b, c, d = split(x)
	e, f, g, h = split(y)

	# Computing the 7 products, recursively (p1, p2...p7)
	p1 = strassen(a, f - h)
	p2 = strassen(a + b, h)
	p3 = strassen(c + d, e)
	p4 = strassen(d, g - e)
	p5 = strassen(a + d, e + h)
	p6 = strassen(b - d, g + h)
	p7 = strassen(a - c, e + f)

	# Computing the values of the 4 quadrants of the final matrix c
	c11 = p5 + p4 - p2 + p6
	c12 = p1 + p2
	c21 = p3 + p4
	c22 = p1 + p5 - p3 - p7

	# Combining the 4 quadrants into a single matrix by stacking horizontally and vertically.
	c = np.vstack((np.hstack((c11, c12)), np.hstack((c21, c22))))

	return c

####################################


# Call the functions.
if __name__ == "__main__":


	# Input two matrices of size n x m
	matrix_A = np.array([[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]])

	matrix_B = np.array([[1, 0, 0, 0],  [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])

	print("Matrix A:\n", matrix_A)
	print("Matrix B:\n", matrix_B)

	print("Matrix C=:\n", strassen(matrix_A, matrix_B))

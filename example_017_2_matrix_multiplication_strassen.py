import numpy as np

def split(matrix):
	'''
	This is a simple split function to divde the input matrices
	'''
	row, col = matrix.shape
	row2, col2 = row//2, col//2
	return matrix[:row2, :col2], matrix[:row2, col2:], matrix[row2:, :col2], matrix[row2:, col2:]


def multi(a, b):
	'''
	Computes matrix product by divide and conquer approach, recursively.
	Input: n x n numpy array matrices a and b
	Output: n x n matrix, product of a and b
	'''

	# Base case when size of matrices is 1x1
	if len(a) == 1:
		return a * b

	# Splitting the matrices into quadrants. This will be done recursively
	# until the base case is reached.
	a11, a12, a21, a22 = split(a)
	b11, b12, b21, b22 = split(b)

	# Computing the values of the 4 quadrants of the final matrix c
	c11 = multi(a11, b11) + multi(a12, b21)
	c12 = multi(a11, b12) + multi(a12, b22)
	c21 = multi(a21, b11) + multi(a22, b21)
	c22 = multi(a21, b12) + multi(a22, b22)

	# Combining the 4 quadrants into a single matrix by stacking horizontally and vertically.
	c = np.vstack((np.hstack((c11, c12)), np.hstack((c21, c22))))

	return c


def strassen(a, b):
	'''
	Computes matrix product by divide and conquer approach, recursively.
	Input: n x n numpy array matrices a and b
	Output: n x n matrix, product of a and b
	'''

	# Base case when size of matrices is 1x1
	if len(a) == 1:
		return a * b

	# Splitting the matrices into quadrants. This will be done recursively
	# until the base case is reached.
	a11, a12, a21, a22 = split(a)
	b11, b12, b21, b22 = split(b)

	# Computing the 7 products, recursively (p1, p2...p7)
	p1 = strassen(a11, b12 - b22)
	p2 = strassen(a11 + a12, b22)
	p3 = strassen(a21 + a22, b11)
	p4 = strassen(a22, b21 - b11)
	p5 = strassen(a11 + a22, b11 + b22)
	p6 = strassen(a12 - a22, b21 + b22)
	p7 = strassen(a11 - a21, b11 + b12)

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

	print("Matrix C=:\n", multi(matrix_A, matrix_B))

	print("Matrix C=:\n", strassen(matrix_A, matrix_B))

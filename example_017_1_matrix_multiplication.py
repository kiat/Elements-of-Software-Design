def multiply_matrix(A,B):
  global C
  if  A.shape[1] == B.shape[0]:
    C = np.zeros((A.shape[0],B.shape[1]),dtype = int)
    for row in range(rows): 
        for col in range(cols):
            for elt in range(len(B)):
              C[row, col] += A[row, elt] * B[elt, col]
    return C
  else:
    return "Sorry, cannot multiply A and B."
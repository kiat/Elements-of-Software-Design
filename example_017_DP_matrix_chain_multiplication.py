# A top-down recursive implementation
import sys


def matrix_chain_recursive(p, i, j):

    if (i == j):
        return 0

    # Set the maximum to be the largest possible number
    # if we get something better than this, then we can swap it
    min = sys.maxsize

# Start generating all possible combinations by brute forcing it and recursive call.
    # This will generate a lots of different combinations that's why our runt time is bad.
    for k in range(i, j):
        count = (matrix_chain_recursive(p, i, k) +
                 matrix_chain_recursive(p, k + 1, j) + p[i-1] * p[k] * p[j])

        if count < min:
            min = count
    # Return minimum count
    return min


def matrix_chain_with_memoization(p, n):
    '''
    Calculates the best minimum operation number of matrix multiplications 
    O(n^3)
    '''
    i = 1
    j = n - 1

    # Create a Dynamic Programming Table to memoize
    dp = [[-1 for i in range(100)] for j in range(100)]

    # Function for matrix chain multiplication

    def matrix_chain_memoization_helper(p, i, j):

        if(i == j):
            return 0

        # if we have already computed it then get it from the memoization table.
        if(dp[i][j] != -1):
            return dp[i][j]

        dp[i][j] = sys.maxsize

        # Otherwise, we compute it using recursion

        for k in range(i, j):
            dp[i][j] = min(dp[i][j], matrix_chain_memoization_helper(p, i, k) +
                           matrix_chain_memoization_helper(p, k + 1, j) + p[i - 1] * p[k] * p[j])

        return dp[i][j]

    return matrix_chain_memoization_helper(p, i, j)


def matrix_chain_bottom_up_iterative(p, n):
    '''This is a bottom up iterative solution with O(n^3) time complexity'''

    dp = [[0 for x in range(n)] for x in range(n)]

    # set the DP table cost for all zero
    for i in range(1, n):
        dp[i][i] = 0

	# iterate over different chain length sizes by going from 2 to n
    for chain_size in range(2, n):
        for i in range(1, n - chain_size + 1):

            j = i + chain_size - 1

            dp[i][j] = sys.maxsize

            for k in range(i, j):
                q = dp[i][k] + dp[k + 1][j] + p[i-1]*p[k]*p[j]

                if q < dp[i][j]:
                    dp[i][j] = q

    return dp[1][n-1]


# Call the functions.
if __name__ == "__main__":
    # A is a 4 × 1 matrix,
    # B is a 1 × 4 matrix, and
    # C is a 4 × 1 matrix.

    # We have two options:
    # 1. (AB) C = (4×1×4) + (4×4×1) = 16 + 16 = 32 operations
    # 2. A (BC) = (1x4x1)+ (1 x 4 x 1) = 4 + 4 = 8 operations

    # Naive Recusive solution Top-Down
    p1 = [4, 1, 4, 1]
    print("The Minimum number of multiplications is: ",
          matrix_chain_recursive(p1, 1, len(p1)-1))

    p2 = [1, 2, 3, 4]
    print("The Minimum number of multiplications is: ",
          matrix_chain_recursive(p2, 1, len(p2)-1))

    # Recursive with Memoization Technique
    print()

    print("The Minimum number of multiplications is: ",
          matrix_chain_with_memoization(p1, len(p1)))

    print("The Minimum number of multiplications is: ",
          matrix_chain_with_memoization(p2, len(p2)))

    ## Buttom Up with Iterations
    print()

    print("The Minimum number of multiplications is: ",
          matrix_chain_bottom_up_iterative(p1, len(p1)))

    print("The Minimum number of multiplications is: ",
          matrix_chain_bottom_up_iterative(p2, len(p2)))

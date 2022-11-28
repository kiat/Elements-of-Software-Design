# Given a set of positive integers 'numbers_list', 
# partition the set of 'numbers_list' into two subsets, S1 and S2, 
# such that the difference between
# the sum of elements in S1 and S2 is minimized. 
# 
# The solution should return the minimum absolute difference between 
# the sum of elements of two partitions.


def find_min_abs_difference(numbers_list, n, sum1=0, sum2=0):

    if n < 0:
        return abs(sum1 - sum2)
 
    option_1 = find_min_abs_difference(numbers_list, n - 1, sum1 + numbers_list[n], sum2)

    option_2 = find_min_abs_difference(numbers_list, n - 1, sum1, sum2 + numbers_list[n])

    # print(option_1, option_2)
 
    return min(option_1, option_2)

###########################################################################
###########################################################################
###########################################################################
###########################################################################

 
def find_min_abs_difference_memoized(numbers_list, n, sum1, sum2, lookup):
    '''Using Memization Technique'''

    # Base case: if the list becomes empty, return the absolute difference between both sets
    if n < 0:
        return abs(sum1 - sum2)

    # Construct a unique key from dynamic elements of the input.
    # Note that we can uniquely identify the subproblem with `n` and `sum1` only
    key = (n, sum1)

    # If the subproblem is seen for the first time, solve it and
    # store its result in a dictionary
    if key not in lookup:

        option_1 = find_min_abs_difference_memoized(numbers_list, n - 1, sum1 + numbers_list[n], sum2, lookup)

        option_2 = find_min_abs_difference_memoized(numbers_list, n - 1, sum1, sum2 + numbers_list[n], lookup)

        lookup[key] = min(option_1, option_2)

        # print(key, min(option_1, option_2))

    return lookup[key]

###########################################################################
###########################################################################
###########################################################################
###########################################################################


def find_min_abs_difference_bottom_up_iterative(numbers_list):

    # Find the sum of all elements
    total = sum(numbers_list)
 
    # Create a boolean table to store solutions to subproblems
    dp = [[False] * (total + 1) for _ in range(len(numbers_list) + 1)]
 
    # Fill the lookup table in a bottom-up manner
    for i in range(len(numbers_list) + 1):
 
        # elements with zero-sum are always true
        dp[i][0] = True
 
        j = 1
        while i > 0 and j <= total:
 
            # exclude the i'th element
            dp[i][j] = dp[i - 1][j]
 
            # include the i'th element
            if numbers_list[i - 1] <= j:
                dp[i][j] |= dp[i - 1][j - numbers_list[i - 1]]
 
            j = j + 1
 
    # Find the maximum value of `j` between 0 and `sum/2` for which the last row is true
    j = total // 2
    while j >= 0 and not dp[len(numbers_list)][j]:
        j = j - 1
 
    return total - 2*j
 


if __name__ == '__main__':
 
    # Input: a set of items
    list_of_numbers = [7, 11, 9, 2]
 
    print('The minimum difference is', find_min_abs_difference(list_of_numbers, len(list_of_numbers) - 1))

    # Here we create a dictionary to store solutions to subproblems
    # This is our memoization table
    lookup = {}

    print('The minimum difference is',  find_min_abs_difference_memoized(list_of_numbers, len(list_of_numbers) - 1, 0, 0, lookup))

    print('The minimum difference is',  find_min_abs_difference_bottom_up_iterative(list_of_numbers))
















# Reference: https://www.techiedelight.com/minimum-sum-partition-problem/#:~:text=Given%20a%20set%20of%20positive,of%20elements%20of%20two%20partitions.

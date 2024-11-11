"""
Simple Dynamic Programming Example 
Finds a pair of numbers in a sequence that sum to a target value.
"""


def pairValues(sequence, target_sum):
    """
    Finds a pair of numbers in a sequence that sum to a target value.
    Args:
    sequence: A list of numbers.
    target: The target value.
    
    Returns:
    A tuple of the two numbers that sum to the target value, or None if no such pair exists.
    """
    for i in range(len(sequence)):
        for j in range(len(sequence)):
            if i != j and sequence[i] + sequence[j] == target_sum:
                return (sequence[i], sequence[j])
    return None


# Using Dynamic Programming

# Using dynamic programming, we can create a dictionary to store the values that are already calculated. 
# The key for the dictionary will be the target value minus the value from the array. 
# If we find a key in the dictionary, we return the pair. 

# A memoized approach

def pairValues_DP(sequence, target_sum):
    
    memoized_set = set()
    
    for num in sequence:
        diff = target_sum - num
        
        if diff in memoized_set:
            return diff, num
        else:
            memoized_set.add(num)

    return None

def main():
    sequence = [8, 10, 2, 9, 7, 5]
    target_sum = 11

    result = pairValues(sequence, target_sum)
    
    print("Pair with sum ", target_sum, " is: ", result)
    
    
    result = pairValues_DP(sequence, target_sum)
    
    print("Pair with sum ", target_sum, " is: ", result)
    
if __name__=="__main__":
    main()
    
    


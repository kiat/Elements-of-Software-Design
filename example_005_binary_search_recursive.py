"""A simple example to demonstrate binary search."""

# Returns True if present, else False


def binary_search(arr, low, high, target):
    """Implementation of binary search with recursive approach."""
    # Check the base case
    if high >= low:

        mid = (high + low) // 2

        # If element is present at the middle itself, then we found it
        if arr[mid] == target:
            return True

        # If element is smaller than mid, then to left subarray
        if arr[mid] > target:
            return binary_search(arr, low, mid - 1, target)

        # Else go to right subarray
        return binary_search(arr, mid + 1, high, target)

    # Element is not present in the array
    return False


# Example Run
ARR = [1, 2, 3, 4, 5]
TARGET = 2

# Function call
result = binary_search(ARR, 0, len(ARR)-1, TARGET)
print(result)


TARGET = 20

# Function call
result = binary_search(ARR, 0, len(ARR)-1, TARGET)
print(result)

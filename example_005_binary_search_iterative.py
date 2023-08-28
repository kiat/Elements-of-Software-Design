"""A simple example to demonstrate binary search."""

def binary_search(data, value):
    """Implementation of binary search with iterative approach."""
    data_len = len(data)
    left = 0
    right = data_len - 1
    count = 0

    while left <= right:
        middle = (left + right) // 2

        count += 1

        if value < data[middle]:
            right = middle - 1
        elif value > data[middle]:
            left = middle + 1
        else:
            return True

    return False


# We have a list like the following data, find the index of it.
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(binary_search(my_list, 6))

print(binary_search(my_list, 60))

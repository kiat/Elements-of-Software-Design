'''Example of merge sort implementation.'''

def merge(arr, left_i, mid_i, right_i):
    '''
    Merge Procedure function of two sorted arrays. Here the two arrays are 
    within the same are on the left and right side. The left side index is from 
    [left to mid] and right side is from [mid to right]
    '''
    n_1 = mid_i - left_i + 1
    n_2 = right_i - mid_i

    # allocate temp lists with sizes of n1 and n2
    left = [0] * n_1
    right = [0] * n_2

    # We copy the data to temp lists of left and right
    for i in range(0, n_1):
        left[i] = arr[left_i + i]

    for j in range(0, n_2):
        right[j] = arr[mid_i + 1 + j]

    # Merge the temp lists back into orginal
    # Initialization
    i = 0           # Initial index of first subarray
    j = 0           # Initial index of second subarray
    k = left_i      # Initial index of merged subarray

    while i < n_1 and j < n_2:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    # Copy the remaining elements of left[]
    while i < n_1:
        arr[k] = left[i]
        i += 1
        k += 1

    # Copy the remaining elements of right[]
    while j < n_2:
        arr[k] = right[j]
        j += 1
        k += 1



def merge_sort(arr, left, right):
    '''Merge sort algorithm'''
    if left < right:

        # Same as (l+r)//2, but avoids overflow for
        # large l and h
        mid = left + (right - left) // 2

        # Sort first and second halves
        merge_sort(arr, left, mid) # recursive call
        merge_sort(arr, mid+1, right) # recursive call
        merge(arr, left, mid, right) # merge them


# Let us test it
my_arr = [9, 12, 18, 5, 6, 7]

print("Given array is:", my_arr)

merge_sort(my_arr, 0, len(my_arr)-1)

print("Sorted array is: ", my_arr)

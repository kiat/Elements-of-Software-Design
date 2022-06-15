
def merge(arr, l, m, r):
    '''Merge Procedure function of two sorted arrays. Here the two arrays are within the same are
    on the left and right side. The left side index is from [l to m ] and right side is from [m, r]'''
    n1 = m - l + 1
    n2 = r - m

    # allocate temp lists with sizes of n1 and n2
    left = [0] * (n1)
    right = [0] * (n2)

    # We copy the data to temp lists of left and right
    for i in range(0, n1):
        left[i] = arr[l + i]

    for j in range(0, n2):
        right[j] = arr[m + 1 + j]

    # Merge the temp lists back into orginal
    # Initialization 
    i = 0     # Initial index of first subarray
    j = 0     # Initial index of second subarray
    k = l     # Initial index of merged subarray

    while i < n1 and j < n2:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    # Copy the remaining elements of left[]
    while i < n1:
        arr[k] = left[i]
        i += 1
        k += 1

    # Copy the remaining elements of right[]
    while j < n2:
        arr[k] = right[j]
        j += 1
        k += 1



def mergeSort(arr, l, r):
    '''Sort merge algorithm'''
    if l < r:

        # Same as (l+r)//2, but avoids overflow for
        # large l and h
        m = l + (r - l) // 2

        # Sort first and second halves
        mergeSort(arr, l, m) # recursive call 
        mergeSort(arr, m+1, r) # recursive call
        merge(arr, l, m, r) # merge them 


# Let us test it 
arr = [9, 12, 18, 5, 6, 7]
n = len(arr)


print("Given array is:", arr)

mergeSort(arr, 0, n-1)

print("Sorted array is: ", arr)


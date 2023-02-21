
# Returns True if present, else False 
def binary_search(arr, low, high, x):
 
    # Check the base case
    if high >= low:
 
        mid = (high + low) // 2
 
        # If element is present at the middle itself, then we found it
        if arr[mid] == x:
            return True
 
        # If element is smaller than mid, then to left subarray
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
 
        # Else go to right subarray
        else:
            return binary_search(arr, mid + 1, high, x)
 
    else:
        # Element is not present in the array
        return False 
 

# Example RUn
arr = [2, 3, 4, 10, 40 ]
x = 10
 
# Function call
result = binary_search(arr, 0, len(arr)-1, x)
print(result)
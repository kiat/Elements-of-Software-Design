def bSearch(data, value):
    n = len(data)
    left = 0
    right = n - 1
    count = 0

    while left <= right:
        middle = (left + right) // 2

        count +=1

        if value < data[middle]:
            right = middle - 1
        elif value > data[middle]:
            left = middle + 1
        else:
            return True

    return False 

# We have a list like the following data, find the index of it.
myList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(bSearch(myList, 6))

print(bSearch(myList, 60))

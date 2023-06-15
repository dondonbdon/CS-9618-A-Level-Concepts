# Given a 1D array of integer data type
arr = [2, 5, 2, 7, 23, 605, 1, 54, 89, 2030, 10]


# function for a linear search to find the value 605 and return its position in the array
def linearSearch(search):
    global arr

    for position in range(len(arr)):
        if search == arr[position]:
            return position

    return None


# function for a binary search to find the value 605 and return its position in the array
def iterativeBinarySearch(search):
    global arr
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (high + low) // 2

        # If element is smaller than mid, then it can only be present in right subarray
        if arr[mid] < search:
            low = mid + 1

        # Else if element is smaller than mid, then it can only be present in left subarray
        elif arr[mid] > search:
            high = mid - 1
        else:
            return mid

    return None

# function for a binary seatch to find the value 605 and return its position in the array
# definition: A subarray is an small array which is from a section of a bigger array
def recursiveBinarySearch(low, high, search):
    global arr
    # Check base case
    if high >= low:

        mid = (high + low) // 2

        # If element is present at the middle itself
        if arr[mid] == search:
            return mid

        # If element is smaller than mid, then it can only be present in left subarray
        elif arr[mid] > search:
            return recursiveBinarySearch(low, mid - 1, search)

        # Else the element can only be present in right subarray
        else:
            return recursiveBinarySearch(mid + 1, high, search)

    else:
        # Element is not present in the array
        return None


# Test search algorithms with test data 5000 and 605
linearSearchResult1 = linearSearch(5000)
linearSearchResult2 = linearSearch(605)
binarySearchResult1 = iterativeBinarySearch(5000)
binarySearchResult2 = iterativeBinarySearch(605)
binarySearchResult3 = recursiveBinarySearch(0, len(arr) - 1, 5000)
binarySearchResult4 = recursiveBinarySearch(0, len(arr) - 1, 605)

if linearSearchResult1 is None:
    print('for linear search, value', 5000, 'was not found')
else:
    print('for linear search, value', 5000, 'was found')

if linearSearchResult2 is None:
    print('for linear search, value', 605, 'was not found')
else:
    print('for linear search, value', 605, 'was found')

if binarySearchResult1 is None:
    print('for iterative binary search, value', 5000, 'was not found')
else:
    print('for iterative binary search, value', 5000, 'was found')

if binarySearchResult2 is None:
    print('for iterative binary search, value', 605, 'was not found')
else:
    print('for iterative binary search, value', 605, 'was found')

if binarySearchResult3 is None:
    print('for recursive binary search, value', 5000, 'was not found')
else:
    print('for recursive binary search, value', 5000, 'was found')

if binarySearchResult4 is None:
    print('for recursive binary search, value', 605, 'was not found')
else:
    print('for recursive binary search, value', 605, 'was found')

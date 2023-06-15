# Function to sort the values in ascending order using bubble sort
def bubbleSort(arr):
    for passes in range(len(arr) - 1):
        for swaps in range(len(arr) - 1 - passes):
            if arr[swaps] > arr[swaps + 1]:
                arr[swaps + 1], arr[swaps] = arr[swaps], arr[swaps + 1]
                # arr[swaps] = arr[swaps + 1] (alternative for above line)
                # arr[swaps + 1] = temp (alternative for above line)

    return arr


# Function to sort the values in ascending order using insertion sort
def insertionSort(arr):
    for i in range(1, len(arr)):

        j = i
        while arr[j] < arr[j - 1] and j > 0:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j -= 1
            # j = j - 1 (alternative for above line)

    return arr


# Function to sort the values in descending order using bubble sort
def bubbleSortReverse(arr):
    for passes in range(len(arr) - 1):
        for swaps in range(len(arr) - 1 - passes):
            if arr[swaps] < arr[swaps + 1]:
                arr[swaps + 1], arr[swaps] = arr[swaps], arr[swaps + 1]
                # temp = arr[swaps] (alternative for above line)
                # arr[swaps] = arr[swaps + 1] (alternative for above line)
                # arr[swaps + 1] = temp (alternative for above line)

    return arr


# Function to sort the values in descending order using insertion sort
def insertionSortReverse(arr):
    for i in range(1, len(arr)):

        j = i
        while arr[j] > arr[j - 1] and j > 0:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j -= 1
            # j = j - 1 (alternative for above line)

    return arr


# Test sorting algorithms by printing old array and new array
print([2, 5, 2, 7, 23, 605, 1, 54, 89, 2030, 10])
print("BUBBLE SORT 1:", bubbleSort([2, 5, 2, 7, 23, 605, 1, 54, 89, 2030, 10]))
print("BUBBLE SORT 2:", bubbleSort([2, 5, 2, 7, 23, 605, 1, 54, 89, 2030, 10]))
print("INSERTION SORT:", insertionSort([2, 5, 2, 7, 23, 605, 1, 54, 89, 2030, 10]))
print("REVERSE BUBBLE SORT:", bubbleSortReverse([2, 5, 2, 7, 23, 605, 1, 54, 89, 2030, 10]))
print("REVERSE INSERTION SORT:", insertionSortReverse([2, 5, 2, 7, 23, 605, 1, 54, 89, 2030, 10]))

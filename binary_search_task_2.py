def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    iterations = 0

    while low <= high:
        iterations += 1
        mid = (high + low) // 2

        # if x is greater than the value in the middle of the list, we ignore the left half
        if arr[mid] < x:
            low = mid + 1

        # if x is less than the value in the middle of the list, ignore the right half
        elif arr[mid] > x:
            high = mid - 1

        # otherwise, x is present at the position and we return the tuple
        else:
            return iterations, arr[mid]

    # if the element is not found, we return a tuple with information about the upper limit
    if low < len(arr):
        return iterations, arr[low]
    else:
        return iterations, None


# ПExample of use:
arr = [1.14, 2.94, 3.96, 4.25, 5.13, 5.6, 6.12, 8.9]
x = 5.13
result = binary_search(arr, x)
iterations, upper_bound = result

print(result)

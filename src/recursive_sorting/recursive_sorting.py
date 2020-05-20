# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    arrA_index = 0
    arrB_index = 0

    for i in range(elements):
        if arrA_index >= len(arrA):
            merged_arr[i] = arrB[arrB_index]
            arrB_index += 1

        elif counter_B >= len(arrB):
            merged_arr[i] = arrA[arrA_index]
            arrA_index += 1

        elif arrA[arrA_index] < arrB[arrB_index]:
            merged_arr[i] = arrA[arrA_index]
            arrA_index += 1
        else:
            # if element in arrB is smaller, add it to merged_arr at that index
            # location and move to next index.
            merged_arr[i] = arrB[arrB_index]
            arrB_index += 1

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    if len(arr) > 1:
        # find the middle of the array [2, 7, 3]
        # left = [2]
        left = merge_sort(arr[0:len(arr)//2])
        # right = [7, 3]
        right = merge_sort(arr[len(arr)//2:])
        # merge halves together
        arr = merge(left, right)

    return arr


# implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # Your code here

    return arr


def merge_sort_in_place(arr, l, r):
    # Your code here

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr

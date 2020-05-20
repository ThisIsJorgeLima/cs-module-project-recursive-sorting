# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)

    total_entries = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # here we initialize our pointers for start of ea. array
    # lets change these to right and left index to make it easier to read further along!
    arrA_left_index = 0
    arrB_right_index = 0

    for i in range(elements):
        # if our left array aka arrA has no more elements to add, append the rest of our right array aka arrB:
        if arrA_left_index == len(arrA):

            while arrB_right_index < len(arrB):
                merged_arr[i] = arrB[arrB_right_index]
                i += 1
                arrB_right_index += 1

            return merged_arr

        # if our right array aka arrB has no elements to add, will append the rest of our left array aka arrA and return:

        elif arrB_right_index == len(arrB):

            while arrA_left_index < len(arrA):
                merged_arr[i] = arrA[arrA_left_index]
                i += 1
                arrA_left_index += 1

        # lets add our entry from our left array if the value is <

        elif arrA[arrA_index_left] < arrB[arrB_index_right]:
            merged_arr[i] = arrA[arrA_index]
            arrA_index_left += 1

        else:
            # if element in arrB is smaller, add it to merged_arr at that index
            # location and move to next index.
            merged_arr[i] = arrB[arrB_index_right]
            arrB_index_right += 1

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # Our base case: if an array of a single element is sorted:
    if len(arr) <= 1:  # : equals the end!

        #  will divide our array into left and right halves:
        right_half = len(arr) // 2

        left = arr[0: right_half]
        right = arr[0: right_half:]
        arr = merge(left, right)  # merge() defined later

        return merge(merge_sort(left), merge_sort(right))

# def merge_in_place(arr, start, mid, end):
#     start_two = mid + 1
#
#     if (arr[mid] <= arr[start2]):
#
#         while (start <= mid and start_two <= end):
#
#             if (arr[start] <= arr[start_two]):
#                 start += 1
#             else:
#                 value = arr[start2]
#                 index = start_two
#
#                 while (index != start):
#                     arr[index] = arr[index - 1]
#                     index -= 1
#                 arr[start] = value
#
#                 start += 1
#                 mid += 1
#                 start_two += 1
#
#     return arr
#
#
# def merge_sort_in_place(arr, l, r):
#     if (1 < r):
#         m = 1 + (r - 1) // 2
#         merge_sort_in_place(arr, 1, m)
#         merge_sort_in_place(arr, m + 1, r)
#
#         merge_in_place(arr, 1, m, r)
#
#         return arr

    # STRETCH: implement the Timsort function below
    # hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt

    # def timsort(arr):
    #     # Your code here
    #
    #     return arr

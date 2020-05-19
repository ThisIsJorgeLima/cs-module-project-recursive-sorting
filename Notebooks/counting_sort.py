# Requires us to know the "max" value that we'll be sorting
# The maximum was arg was so we could specify the max value
# The total range of data we'll be sorting sits between 0 and maximum
# O(max + n)
# O(max) space complexity


def counting_sort(arr, maximum=-1):
    if len(arr) == 0:  # O(1)
        return arr  # O(1)

    # if maximum is not given, we'll take the max value from the input array
    if maximum == -1:  # O(1)
        maximum = max(arr)  # O(n)

    # make a bunch of buckets
    buckets = [0 for _ in range(maximum+1)]  # O(max)

    for x in arr:  # O(n)
        if x < 0:
            return "Error, negative numbers not allowed"
        buckets[x] += 1  # O(1)

    # we have the counts of every value in our input array
    # loop through our buckets, starting at the smallest index
    # j keeps track of the spot we're writing to in our input array
    j = 0

    # this whole loop is reversing the tallying we did in the previous loop

    # max - n = diff
    for i in range(len(buckets)):  # O(max)
        while buckets[i] > 0:
            arr[j] = i
            j += 1
            buckets[i] -= 1

    return arr


arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]

print(counting_sort(arr1))

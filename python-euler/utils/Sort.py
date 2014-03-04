# Merge Sort: Always O(n*log(n))
# Quick Sort:
#     Best Case: O(n*log(n))
#     Worst Case: O(n**2)

# Merge sort is better when space is a non-issue. Quick sort is better when space is an issue.

# Merge Sort [O(n*log(n))]
# Performs a merge sort on the passed in array. Algorithm:
#   1. Divide the unsorted list into n sublists, each containing 
#      1 element (a list of 1 element is considered sorted).
#   2. Repeatedly merge sublists to produce new sorted sublists 
#      until there is only 1 sublist remaining. This will be the 
#      sorted list.

def merge(left, right):
    """
    left, right: lists of elements to merge
    O(N)

    Performs merge portion of merge sort algorithm. While both lists
    have elements, append the smaller value of each list until one 
    list is depleted. Once depleted, merge the remaining portion of
    the non-empty list.
    """
    result = []
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        elif len(left) > 0:
            result.append(left.pop(0))
        elif len(right) > 0:
            result.append(right.pop(0))
    return result

def merge_sort(array):
    """
    array: list to sort
    O(log(n))

    Recursive function to perform merge sort algorithm.
    Base Case: Length of Array <= 1 return Array
    Recursive Case:
        1. Split array in halfs then recursively split.
        2. Once reached base case, return merged smaller lists.
    """
    length = len(array)
    if length <= 1:
        return array
    left = merge_sort(array[:length/2])
    right = merge_sort(array[length/2:])
    return merge(left, right)


# Quick Sort [O(n*log(n))]
# Algorithm:
#     1. Pick an element, called a pivot, from the list.
#     2. Reorder the list so that all elements with values 
#        less than the pivot come before the pivot, while 
#        all elements with values greater than the pivot 
#        come after it (equal values can go either way). 
#        After this partitioning, the pivot is in its final 
#        position. This is called the partition operation.
#     3. Recursively apply the above steps to the sub-list 
#        of elements with smaller values and separately the 
#        sub-list of elements with greater values.

def pick_pivot(array):
    """
    Picks the index of the median of the first, middle and 
    last elements of a list to be the pivot point. This 
    version of the pivot function almost guarantees 
    O(n*log(n)) on each run.
    """
    length = len(array)
    if length % 2 == 0:
        options = [array[0], array[length/2 - 1], array[-1]]
    else:
        options = [array[0], array[length/2], array[-1]]
    return array.index(sorted(options)[1])

def partition(array):
    """
    Runs quick sorts partition function. Essentially, take
    all elements less than the pivot and move it to the left
    of the pivot in the list and leave everything else to right.
    Return the pivot's index for the recursive step of quick sort.
    """
    pivot_value = array[0]
    i = 1
    for j in xrange(1, len(array)):
        if array[j] < pivot_value:
            array[i], array[j] = array[j], array[i]
            i += 1
    pivot = i - 1
    array[0], array[pivot] = array[pivot], array[0]
    return pivot

def quick_sort(array):
    """
    Recursive function to perform quick sort algorithm.
    Base Case: Length of Array <= 1 return Array
    Recursive Case:
        1. Find pivot and move to head of array
        2. Run partition function to get all elements
           less than the pivot to the left of it and all
           elements greater to the right.
        3. Recursively call quick sort on the left and 
           right partitions of the array.
    """
    if len(array) <= 1:
        return array
    pivot = pick_pivot(array)
    array[0], array[pivot] = array[pivot], array[0]
    pivot = partition(array)
    return quick_sort(array[:pivot]) + array[pivot:pivot+1] + quick_sort(array[pivot+1:])
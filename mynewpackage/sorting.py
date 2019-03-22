def bubble_sort(items):

    '''Return array of items, sorted in ascending order'''
    for i in range(len(items)):
        for j in range(len(items)-1-i):
            if items[j] > items[j+1]:
                items[j], items[j+1] = items[j+1], items[j]

    return items


# Merge sort returns a sorted list.
def merge_sort(items):

    len_i = len(items)
    # Base case. A list of size 1 is sorted.
    # Cae returns, so if reached then function will terminate after line 8
    if len_i == 1:
        return items
    # Recursive case. Find midpoint of list
    mid_point = int(len_i / 2)
    # divide list into two halves
    i1 = merge_sort(items[:mid_point])
    i2 = merge_sort(items[mid_point:])
    # call merge_sort function on each half of list


# Merge function.
    def merge(A, B):
        new_list = []
        while len(A) > 0 and len(B) > 0:
            if A[0] < B[0]:
                new_list.append(A[0])
                A.pop(0)
            else:
                new_list.append(B[0])
                B.pop(0)

        if len(A) == 0:
            new_list = new_list + B
        elif len(B) == 0:
            new_list = new_list + A

        return new_list

    return merge(i1, i2)

def quick_sort(items):

    '''Return array of items, sorted in ascending order'''
    length_items = len(items)

    if length_items <= 1:
        return items

    pivot = items[-1]
    small = []
    large = []
    duplicate = []

    for i in items:
        if i < pivot:
            small.append(i)
        elif i > pivot:
            large.append(i)
        elif i == pivot:
            duplicate.append(i)

    small = quick_sort(small)
    large = quick_sort(large)

    return small + duplicate + large

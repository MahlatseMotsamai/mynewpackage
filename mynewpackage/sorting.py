def bubble_sort(items):

    '''Return array of items, sorted in ascending order'''
    for i in range(len(items)):
        for j in range(len(items)-1-i):
            if items[j] > items[j+1]:
                items[j], items[j+1] = items[j+1], items[j]

    return items


def merge_sort(items):

    '''Return array of items, sorted in ascending order'''
    def lin_merge(list1, list2):

        new_list = []
        while (len(list1) > 0  and len(list2) > 0):
            if list1[0] < list2[0]:
                new_list.append(list1.pop(0))
            else:
                new_list.append(list2.pop(0))

        return new_list + list1 + list2

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

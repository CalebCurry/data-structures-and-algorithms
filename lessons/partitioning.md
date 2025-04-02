# Hoare's Partitioning Algorithm

Partitioning causes the data of an array to be arranged based on a chosen **pivot**. This is a chosen value used to split the data.

Elements less than the pivot go to its left and elements greater go to its right.

This does not sort the data entirely, it only places any smaller elements to the left and any larger elements to the right. Partitioning doesn’t care about precise sorted order of elements.

Say we start with an array `[12, 4, 6, 40, 3, 9, 10]` and `pivot = 12` (index 0). We could end up with `[9, 4, 6, 10, 3, 12, 40]`. The result is not fully sorted, but all elements less than `12` are on the left and all elements larger are on the right.

```python
def partition(data, left=0, right=None):
    if not right:
        right = len(data) - 1

    if len(data) <= 1:
        return 0

    pivot = data[left]

    low = left + 1
    high = right

    while True:
        while low <= high and data[low] < pivot:
            low += 1

        while high >= low and data[high] > pivot:
            high -= 1


        if low >= high:
            # Move pivot to correct position
            data[left], data[high] = data[high], data[left]
            return high

        data[low], data[high] = data[high], data[low]

        # move both pointers after swap
        low += 1
        high -= 1


data = [12, 4, 6, 40, 3, 9, 10]
partition(data)
print(data) # [9, 4, 6, 10, 3, 12, 40]
```

I made it so that we use `left` and `right` passed in which will make this function useful for quicksort where we are not always looking at the full array.

# Quicksort

Quick Sort is the algorithm most known to use this array partitioning approach. Now that we have `partition` we can create a `quicksort` function that utilizes it.

Quick sort is a **divide and conquer** algorithm which breaks up a problem in to smaller sub problems. The partition splits the array in to two, returning the pivot's final index. In the code example we invoke `quicksort` recursively, once for the data on the left of the pivot and once for the data on the right side of the pivot.

```python
def quicksort(data, left=0, right=None):
    if right is None:
        right = len(data) - 1

    if left < right:
        p = partition(data, left, right)

        quicksort(data, left, p)
        quicksort(data, p + 1, right)


data = [12, 4, 6, 40, 3, 9, 10]
quicksort(data)
print(data) # [3, 4, 6, 9, 10, 12, 40]
```

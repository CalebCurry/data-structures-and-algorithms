# Hoare's Partitioning Algorithm

Partitioning causes the data of an array to be arranged based on a chosen **pivot**. This is a chosen value used to split the data.

Elements less than the pivot go to its left and elements greater go to its right.

This does not sort the data entirely, it only places any smaller elements to the left and any larger elements to the right. Partitioning doesn’t care about precise sorted order of elements.

Say we start with an array `[4, 6, 12, 40, 3, 9, 10]` and `pivot = 12`. We could end up with `[9, 6, 4, 10, 3, 12, 40]`. The result is not fully sorted, but all elements less than `12` are on the left and all elements larger are on the right.

```python
def partition(data, pivot_index=0):
    if len(data) <= 1:
        return 0

    # Move pivot to the start
    data[0], data[pivot_index] = data[pivot_index], data[0]
    pivot = data[0]

    low = 1
    high = len(data) - 1

    while True:
        while low <= high and data[low] < pivot:
            low += 1

        while high >= low and data[high] > pivot:
            high -= 1


        if low >= high:
            # Move pivot to correct position
            data[0], data[high] = data[high], data[0]
            return high

        data[low], data[high] = data[high], data[low]

        # move both pointers after swap
        low += 1
        high -= 1


data = [4, 6, 12, 40, 3, 9, 10]
partition(data, pivot_index=2)

print(data) #[9, 6, 4, 10, 3, 12, 40]
```

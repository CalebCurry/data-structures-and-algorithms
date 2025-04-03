# Hoare's Partitioning Algorithm

Partitioning causes the data of an array to be arranged based on a chosen **pivot**. This is a chosen value used to split the data.

Elements less than the pivot go to its left and elements greater go to its right.

This does not sort the data entirely, it only places any smaller elements to the left and any larger elements to the right. Partitioning doesn’t care about precise sorted order of elements.

Say we start with an array `[12, 4, 6, 40, 3, 9, 10]` and `pivot = 12` (index 0). We could end up with `[9, 4, 6, 10, 3, 12, 40]`. The result is not fully sorted, but all elements less than `12` are on the left and all elements larger are on the right.

The algorithm works by setting a pivot value, often the value at index 0. We then have a `low` pointer and `high` pointer. These two pointers move towards each other. We first move `low` to the right until it finds a value greater than the pivot. We then move `high` to the left until it finds a value less than the pivot. When these values are found we swap them and continue moving `low` and `high` inward.

Eventually the `low` and `high` pointers will collide meaning we've gone through the entire array. Where these pointers collide is the splitting point between values lower than the pivot and values higher than the pivot.

After the pointers collide we swap the pivot (`data[left]`) with the `high` pointer (`data[high]`) placing the pivot between the lesser values and greater values.

```python
def partition(data, left=0, right=None):
    if right is None:
        right = len(data) - 1

    if len(data) <= 1:
        return 0

    pivot = data[left]

    low = left + 1
    high = right

    while low < high:
        if data[low] < pivot:
            low += 1

        elif data[high] > pivot:
            high -= 1

        else:
            data[low], data[high] = data[high], data[low]
            low += 1
            high -= 1


    # Move pivot to correct position
    data[left], data[high] = data[high], data[left]
    return high



data = [12, 4, 6, 40, 3, 9, 10]
partition(data)
print(data) # [9, 4, 6, 10, 3, 12, 40]
```

I made it so that we use `left` and `right` passed in instead of always using the ends of the full array. This makes the function useful for algorithms where we are not always looking at the full array.

## Quick Select

We can utilize partitioning to partially sort an array and find the kth smallest or largest element, where we provide the value for `k`.  
For example, the 3rd smallest element in `[12, 4, 6, 40, 3, 9, 10]` is `6`.

Instead of sorting everything, partitioning will split the data in to larger and smaller than the random pivot. We will then repeat the process with just the partition that the `kth` element would be in. Effectively, we are cutting the search space in half with each iteration.

```python
import random
def quick_select(data, kth):
    start = 0
    end = len(data) - 1
    #adjust to zero based
    k_index = kth - 1

    while start <= end:
        #randint is inclusive
        r = random.randint(start, end)

        #place this pivot at index 0
        data[start], data[r] = data[r], data[start]
        pivot = partition(data, start, end)

        if pivot == k_index:
            return pivot

        if pivot < k_index:
            start = pivot + 1
        else:
            end = pivot - 1

data = [12, 4, 6, 40, 3, 9, 10]
index = quick_select(data, 3)
print(index, data[index]) #2 6
```

This tells us that the 3rd smallest element in this array is `6` without having to sort the complete array.

To convert this example to the kth largest element we can change the `k` argument passed. Consider a dataset with 10 elements, the 4th largest is also the 7th smallest. To get from `4` to `7` we can do `k_smallest = len(data) - k + 1`. You can think of finding the kth largest as finding the element k positions from the end of a sorted array.

## Exercise - Find the kth Highest Score

Using what we've learned so far, given an array `scores = [10, 70, 80, 90, 20, 30, 40, 50, 60, 100]`, return the 4th highest score in the list.

<details>
<summary>Solution</summary>

The goal is to find 4th biggest. We know it is 70 by looking at the sorted array for practice. 70 is at index 6 and is the 7th smallest.  
Convert to 7th smallest with `len(data) - k + 1`

```python
scores = [10, 70, 80, 90, 20, 30, 40, 50, 60, 100]

# for practice you can see the sorted array

print(sorted(scores)) # [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

k = 4 #4th largest
k_smallest = len(scores) - k + 1 #7th smallest

print(scores[quick_select(scores, k_smallest)]) #70

```

</details>

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

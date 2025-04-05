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

Instead of sorting everything, partitioning will split the data in to larger and smaller than the random pivot. We will then repeat the process with just the partition that the `kth` element would be in.

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

The goal is to find 4th largest. We know it is 70 by looking at the sorted array for practice. 70 is at index 6 and is the 7th smallest.  
Convert to 7th smallest with `len(data) - k + 1`

```python
scores = [10, 70, 80, 90, 20, 30, 40, 50, 60, 100]

# For practice you can see the sorted array
print(sorted(scores)) # [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

k = 4 # 4th largest
k_smallest = len(scores) - k + 1 # 7th smallest

print(scores[quick_select(scores, k_smallest)]) # 70

```

</details>

## Exercise - Find the Top k Scores

In the previous exercise we retrieved the top 4th value.  
How would you change things if you didn't just want the the top 4th, but also the top 3rd, 2nd, and 1st.  
We want an array of the top 4 values, not just one.

Assume we found the top kth element, the way partitioning works means that all elements greater than `data[k]` are on the right side of `k`. We can take that entire partition to retrieve the full array. Partitioning doesn't guarantee complete order, it only guarantees that each element is larger than `data[k]`. This means we will need to sort the partition.

Find the top 4 elements of `scores`.
scores = [10, 70, 80, 90, 20, 30, 40, 50, 60, 100]

<details>
<summary>Solution</summary>

We will use slicing to retrieve all elements from k to the end: `[kth_position:]`

```python

k = 4 #4th largest
k_smallest = len(scores) - k + 1 # 7th smallest

kth_position = quick_select(scores, k_smallest)
top_k = sorted(scores[kth_position:])
print(top_k)
```

</details>

## Exercise - Pixel Color Grouping

You are given an array of RGB pixel values, where each pixel is represented as a tuple (r, g, b) with integer values for red (r), green (g), and blue (b) components, each ranging from 0 to 255. The task is to group the pixels based on their perceived "color similarity" to a target color. We'll define color similarity based on the Euclidean distance in RGB space.

### Inputs:

-   pixels: An array of RGB pixel tuples.
-   target_color: An RGB tuple representing the target color (r_target, g_target, b_target).
-   threshold: A float representing the maximum Euclidean distance for a pixel to be considered "similar" to the target_color.

### Constraints:

The input pixels array will contain valid RGB tuples.
0 <= r, g, b <= 255 for all pixels.
threshold >= 0

### Output

All pixels whose Euclidean distance to the target_color is less than the threshold are placed on the left side of the array.
Note: The Euclidean distance between two RGB colors (r1, g1, b1) and (r2, g2, b2) is calculated as:

```python
distance = sqrt((r1 - r2)^2 + (g1 - g2)^2 + (b1 - b2)^2)
```

<details>
<summary>Solution</summary>

```python
from math import sqrt

pixels = [
(132, 123, 12),
(12, 23, 190),
(132, 103, 120),
(45, 67, 200),
(123, 111, 30),
(80, 90, 160),
(150, 140, 10),
(25, 35, 180),
(100, 120, 100),
(60, 75, 220),
]
target_color = (100, 100, 100)
threshold = 100

distances = []
r2, g2, b2 = target_color[0], target_color[1], target_color[2]

for pixel in pixels:
r1, g1, b1 = pixel[0], pixel[1], pixel[2]
distances.append(sqrt((r1 - r2)**2 + (g1 - g2)**2 + (b1 - b2)\*\*2))

distances.insert(0, threshold) # insert threshold at start of array

# if needed
# distances.pop(partition(distances)) # remove threshold from array

print(distances)

# [100, 96.42095207992918, 147.5567687366459, 37.8549864614954,
# 118.80235687897779, 74.4983221287567, 64.03124237432849,
# 110.45361017187261, 127.47548783981962, 20.0, 128.93796958227628]

</details>
```

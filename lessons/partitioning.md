# Hoare's Partitioning Algorithm

Partitioning causes the data of an array to be arranged based on a chosen **pivot**. This is a chosen value used to split the data.

Elements less than the pivot go to its left and elements greater go to its right.

This does not sort the data entirely, it only places any smaller elements to the left and any larger elements to the right. Partitioning doesn’t care about precise sorted order of elements.

Say we start with an array `[4, 6, 12, 40, 3, 9, 10]` and `pivot = 12`. We could end up with `[4, 6, 3, 9, 10, 12, 40]`. The result is not sorted, but all elements less than `12` are on the left and all elements larger are on the right.

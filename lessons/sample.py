def partition(data):
    low = 1
    high = len(data) - 1
    pivot = data[0]
    
    while low <= high:
        while data[low] < pivot:
            low += 1
            
        while data[high] > pivot:
            high -= 1

        data[low], data[high] = data[high], data[low]

        low += 1
        high -= 1


data = [4, 6, 12, 40, 3, 9, 10]
partition(data)
print(data)
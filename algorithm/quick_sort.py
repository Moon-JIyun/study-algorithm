num = [40,35,27,75,66,32,11,234,55,13,26]

def quickSort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [num for num in arr[1:] if num <= pivot]
        bigger = [num for num in arr[1:] if num >= pivot]
        return quickSort(less) + [pivot] + quickSort(bigger)

result = quickSort(num)
print(result)

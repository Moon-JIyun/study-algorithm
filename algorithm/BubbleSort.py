#핵심로직 : 첫번째꺼랑 두번째꺼랑 비교해서 두번째꺼가 더 작으면 첫번째꺼랑 자리 바꾼다.

num = [40,35,27,75,66,32,11,234,55,13,26]

def BubbleSort(arr):
    for j in range(len(arr)-1):
        for i in range(j+1, len(arr)):
            if arr[j] > arr[i]:
                temp = arr[j]
                arr[j] = arr[i]
                arr[i] = temp
    return arr

result = BubbleSort(num)
print(result)
def findMin (arr):
    min = arr[0]
    min_indice = 0
    for i in range(len(arr)):
        if arr[i] < min:
            min = arr[i]
            min_indice=i
    return min_indice

def orderList (arr):
    newArr= []

    for i in range(len(arr)):
        min = findMin(arr)
        newArr.append(arr.pop(min))
    return newArr


print(orderList([5,2,3]))
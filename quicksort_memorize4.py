def binary_search(array, item):
    min = 0
    max = len(array)
    while min<=max:
        half = (min + max)//2
        attempt = array[half]
        if attempt == item:
            return half
        if attempt>item:
            max = half -1
        else:
            min = half +1
    return None


print(binary_search([3,5,7],5))


def quicksort(arr):
    if len(arr) <=2:
        return arr
    else:
        aux = arr[0]
        menores=[i for i in arr[1:] if i <= aux]
        maiores = [i for i in arr[1:] if i> aux]

        return quicksort(menores) + [aux] + quicksort(maiores)


print(quicksort([3,6,2]))


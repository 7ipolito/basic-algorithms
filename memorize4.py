def binary_search (list, item):
    min = 0
    max = len(list) -1

    while min<=max:
        half = (min+max) //2
        attempt = list[half]

        if attempt == item :
            return half
        if attempt>item:
            max = half -1
        else:
            min = half +1
    return None


list_o= [3,6,7,10,90]

print(binary_search(list_o,6))

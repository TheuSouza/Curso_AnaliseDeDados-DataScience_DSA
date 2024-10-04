def buble_sort(array=list) -> list:

    n = len(array)

    for i in range(0, n):
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
        
    return array


numeros = [5, 4, 8, 9, 11, 43, 56, 78, 12, 99, 59, 2, 66, 41, 47, 3, 8, 51]
array_ordenado = buble_sort(numeros)
print(f'Lista ordenada: {array_ordenado}')


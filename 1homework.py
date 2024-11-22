def revers_func(array):
    #Берём односвязный список и с помощью цыкла for достаем все элементы списка от последнего до первого.
    #После чего записываем каждый элемент в новый, пустой список и возвращаем его
    new_array = []
    for symbol in range(len(array), 0, -1):
        new_array.append(array[symbol-1])
    return new_array
array = [5, 4, 3, 2, 1]
print(revers_func(array))
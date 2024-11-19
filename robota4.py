def selection_sort(array, order="ascending"):
    n = len(array)
    for i in range(n):
        index = i
        for j in range(i + 1, n):
            if (order == "ascending" and array[j] < array[index]) or \
                    (order == "descending" and array[j] > array[index]):
                index = j

        array[i], array[index] = array[index], array[i]
    return array


список_1 = [64, 34, 25, 12, 22, 11, 90]
список_2 = [5, 8, 1, 3, 7, 9, 2]

print("Сортування за зростанням:")
print(selection_sort(список_1, "ascending"))
print(selection_sort(список_2, "ascending"))

print("\nСортування за спаданням:")
print(selection_sort(список_1, "descending"))
print(selection_sort(список_2, "descending"))


# ----------------------------------------------------------------------------#
# s = ['BMW', 'Ford', 'Volvo']
# a = [1, 45, 4, 56, 3, 2]
# b = [1, 45, 4, 56, 3, 2]
# s.sort()               # Создает новый список
# print(s)
# a.sort()
# print(a)
# print(sorted(b))


#                             Bubble sort
# ----------------------------------------------------------------------------#
import  time
from random import randint

a = [randint(1, 100) for i in range(100)]
# Option 1
# flag = True
# while flag:
#     flag = False
#     for i in range(len(a)-1):
#          if a[i] > a[i+1]:
#             a[i], a[i+1] = a[i + 1], a[i]
#             flag = True
# print(a)

# Option 2
start = time.time()

for i in range(len(a)):
    for j in range(0, len(a) - i - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]


  #  or --> # temp = a[j]
            # a[j] = a[j+1]
            # a[j+1] = temp
print(a)
end = time.time()
print("Сотировка пузырьками: ", end-start)


# #                     Сортировка Вставками  (Insertion Sort) 
# # ----------------------------------------------------------------------------#
start1 = time.time()
lst = [randint(1 , 100) for i in range(100)]

for i in range(1, len(lst)):
    key = lst[i]
    j = i - 1
    while j >= 0 and key < lst[j]:
        lst[j + 1] = lst[j]
        j -= 1
    lst[j + 1] = key

print(lst)

end1 = time.time()
print("Сотировка вставками: ", end1 - start1)


#                     Сортировка слиянием (Merge Sort)
# ----------------------------------------------------------------------------#

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    # Разделение массива на две половины
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # Рекурсивная сортировка каждой половины 
    left_half = merge_sort(left_half)  
    right_half = merge_sort(right_half)
    
    # Объединение отсортированных половин
    return merge(left_half, right_half)

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0
     
    # Слияние двух отсортированных половин
    
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
    
    # Добавление оставшихся элементов
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    return merged
start2 = time.time()
print(merge_sort(lst))
end2 = time.time()
print('Сортировка слиянием: ', end2 - start2)
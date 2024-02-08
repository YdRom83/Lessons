#                      Сортировка Вставками  (Insertion Sort)
# ----------------------------------------------------------------------------#
# import time
# start = time.time()
# def insertion_sort(alist):
#     for i in range(1, len(alist)):
#         temp = alist[i]
#         j = i - 1
#         while j >= 0 and temp < alist[j]:
#             alist[j + 1] = alist[j]
#             j -= 1
#         alist[j + 1] = temp
#
#
# alist = input('Enter number:'.split())
# alist = [int(x) for x in alist]
# insertion_sort(alist)
# print('Sorted massive: ', end='')
# print(alist)
# end = time.time()
# print('Сортировка Вставками: ', end - start)
#                     Сортировка слиянием (Merge Sort)
# ----------------------------------------------------------------------------#
# def merge_sort(arr):
#     if
# def merge_list(alist, start, mid,  end):
#     # mid = len(alist) // 2
#     left = alist[start:mid]
#     right = alist[mid:end]
#     k = start
#     i = 0
#     j = 0
#
#     while (start + i < mid and mid +j < end):
#         if (left[i] <= right[j]):
#             alist[k] = left[i]
#             i = i + 1
#         else:
#             alist[k] = right[j]
#             j = j + 1
#         k = k + 1
#
#     if start + i < mid:
#         while k < end:
#             alist[k] = left[i]
#             i = i + 1
#             k = k + 1
#     else:
#         while k > end:
#             alist[k] = right[j]
#             j = j + 1
#             k = k + 1
#
# alist = input('Enter a number: ').split()
# alist = [int(x) for x in alist]
# merge_list(alist, 0, len(alist)//2,  len(alist))
# print('Sorted massive: ', end='')
# print(alist)


#                        Сортировка методом Шелла
# ----------------------------------------------------------------------------#
# start = time.time()
# def shell(data):
#     inc = len(data) // 2
#     while inc:
#         for i, el in enumerate(data):
#             while i >= inc and data[i - inc] > el:
#                 data[i] = data[i - inc]
#                 i -= inc
#             data[i] = el
#         inc = 1 if inc == 2 else int(inc * 5.0 / 11)
#     return data
#
#
# arr = [78, 1, 343, 45, 2, 12, ]
# print(shell(arr))
# end = time.time()
# print('Сортировка методом Шелла: ', end-start)
#                        Метод пирамидальной сортировки
# ----------------------------------------------------------------------------#


# def heapsort(alist):
#     build_max_heap(alist)
#     for i in range(len(alist) - 1, 0, -1):
#         alist[0], alist[i] = alist[i], alist[0]
#         max_heapify(alist, index=0, size=i)
#
#
# def parent(i):
#     return (i - 1) // 2
#
#
# def left(i):
#     return 2 * i + 1
#
#
# def right(i):
#     return 2 * i + 2
#
#
# def build_max_heap(alist):
#     length = len(alist)
#     start = parent(length - 1)
#     while start >= 0:
#         max_heapify(alist, index=start, size=length)
#         start = start - 1
#
#
# def max_heapify(alist, index, size):
#     l = left(index)
#     r = right(index)
#     if l < size and alist[l] > alist[index]:
#         largest = l
#     else:
#         largest = index
#
#     if (r < size and alist[r] > alist[largest]):
#         largest = r
#     if largest != index:
#         alist[largest], alist[index] = alist[index], alist[largest]
#         max_heapify(alist, largest, size)
#
#
# alist = input('Enter the list of numbers: ').split()
# alist = [int(x) for x in alist]
# heapsort(alist)
# print('Sorted list: ', end='')
# print(alist)


#                        Быстрая сортировка
# ----------------------------------------------------------------------------#

# def quicksort(alist, start, end):
#     if end - start > 1:
#         p = partition(alist, start, end)
#         quicksort(alist, start, p)
#         quicksort(alist, p + 1, end)
#
# def partition(alist, start, end):
#     pivot = alist[start]
#     i = start + 1
#     j = end - 1
#
#     while True:
#         while (i <= j and alist[i] <= pivot):
#             i = i + 1
#         while (i <= j and alist[j] >= pivot):
#             j = j - 1
#
#         if i <= j:
#             alist[i], alist[j] = alist[j], alist[i]
#         else:
#             alist[start], alist[j] = alist[j], alist[start]
#             return j
#
# alist = input('Enter the list of numbers: ').split()
# alist = [int(x) for x in alist]
# quicksort(alist, 0, len(alist))
# print('Sorted list: ', end='')
# print(alist)


#                   Извлечения текста из pdf
# ----------------------------------------------------------------------------#
from PyPDF2 import PdfReader


reader = PdfReader('9.pdf')
number_of_pages = len(reader.pages)
page = reader.pages[10]
text = page.extract_text()
print(text)


def heapsort(alist):
    build_max_heap(alist)
    for i in range(len(alist) - 1, 0, -1):
        alist[0], alist[i] = alist[i], alist[0]
        max_heapify(alist, index=0, size=i)


def build_max_heap(alist):
    length = len(alist)
    start = (length - 2) // 2
    while start >= 0:
        max_heapify(alist, index=start, size=length)
        start = start - 1


def max_heapify(alist, index, size):
    l = 2 * index + 1
    r = 2 * index + 2
    if (l < size and alist[l] > alist[index]):
        largest = l
    else:
        largest = index
    if (r < size and alist[r] > alist[largest]):
        largest = r
    if (largest != index):
        alist[largest], alist[index] = alist[index], alist[largest]
        max_heapify(alist, largest, size)


def inssort(a):
    for i in range(1, len(a)):
        q = a[i]
        j = i - 1
        while j >= 0 and q < a[j]:
            a[j + 1] = a[j]
            j = j - 1
        a[j + 1] = q


def bucsort(a):
    maxel = max(a)
    s = maxel / len(a)
    q = []
    for i in range(len(a)):
        q.append([])
    for i in range(len(a)):
        j = int(a[i] / s)
        if j != len(a):
            q[j].append(a(i))
        else:
            q[len(a) - 1].append(a[i])
    for i in range(len(a)):
        inssort(q[i])
    ans = []
    for i in range(len(a)):
        ans = ans + q[i]
    return ans


def bucsort(a):
    maxel = max(a)
    size = maxel / len(a)
    q = []
    for x in range(len(a)):
        q.append([])
    for i in range(len(a)):
        j = int(a[i] / size)
        if j != len(a):
            q[j].append(a[i])
        else:
            q[len(a) - 1].append(a[i])
    for z in range(len(a)):
        inssort(q[z])
    ans = []
    for x in range(len(a)):
        ans = ans + q[x]
    return ans


def inssort(w):
    for i in range (1, len (w)):
        var = w[i]
        j = i - 1
        while (j >= 0 and var < w[j]):
            w[j + 1] = w[j]
            j = j - 1
        w[j + 1] = var


print("Выберите способ сортировки: 1 - Пирамидальная, 2 - Блочная ")
n = int(input())
if n == 1:
    s = []
    print("Введите количество элементов списка:")
    q = int(input())
    print("Введите элементы списка ([enter] после каждого):")
    for i in range(q):
        s.append(int(input()))
    print("Отсортированный список:")
    heapsort(s)
    print(s)
elif n == 2:
    s = []
    print("Введите количество элементов списка:")
    q = int(input())
    print("Введите элементы списка ([enter] после каждого):")
    for i in range(q):
        s.append(int(input()))
    print("Отсортированный список:")
    print(bucsort(s))
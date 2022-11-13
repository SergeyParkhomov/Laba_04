import Module1

print("Выберите метод сортировки: 1 - Быстрая сортировка, 2 - Сортировка расческой")
n = int(input())
if n == 1:
    s = []
    print("Введите количество элементов списка:")
    q = int(input())
    print("Введите элементы списка ([enter] после каждого):")
    for i in range(q):
        s.append(int(input()))
    print("Отсортированный список:")
    print(Module1.fastsort(s))
elif n == 2:
    s = []
    print("Введите количество элементов списка:")
    q = int(input())
    print("Введите элементы списка ([enter] после каждого):")
    for i in range(q):
        s.append(int(input()))
    print("Отсортированный список:")
    print(Module1.rassort(s))

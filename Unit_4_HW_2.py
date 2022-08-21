# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Сдвиньте все элементы списка на 2 позиции вправо.
# 3 -> [2, 3, -3, -2, -1, 0, 1]

number = int(input("Введите число "))
number = abs (number)
values = list(range(-number, number+1))
steps = 2

values = values[-steps:] + values[:-steps]
print(values)
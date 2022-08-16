# Задача 1. Напишите программу, которая принимает на вход число N и выдает список факториалов для чисел от 1 до N.
# пусть N = 4 -> [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def factorial (x):
    list = [1]*x
    for i in range(2, x+1):
        for j in range(1, i+1):
            list[i-1] = list[i-1] * j
    return list


N = int(input("Введите число: "))
print(factorial(N))
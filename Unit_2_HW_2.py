# Задача 2. Выведите таблицу истинности для выражения ¬(X ∧ Y) ∨ Z.

def check():
    for x in range(2):
        for y in range(2):
            for z in range(2):
                print(x, y, z, int(not (x and y) or z))

print("X", "Y", "Z", "¬X∨Y")
check()

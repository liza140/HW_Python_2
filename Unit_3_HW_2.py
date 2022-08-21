# Задача 3. Даны две строки. Посчитайте сколько раз каждый символ первой строки встречается во второй
# «one» «onetwonine» - o – 2, n – 3, e – 3

def countSimb (first_string: str, second_string: str):
    dictionary = []
    for letter in first_string:
        if letter not in dictionary:
            dictionary.append(letter)
            count = 0
            for symbol in second_string:
                if letter == symbol:
                    count +=1
            print(f"Буква '{letter}' встречается в '{second_string}' {count} раз(-а)")
        else:
            print(f"Буква '{letter}' уже встречалась")

string_1 = 'oneo'
string_2 = 'onetwonine'
count_list = countSimb (string_1, string_2)

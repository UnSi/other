# Угадай число

import random

number = random.randint(1,100)
print(number)

while True:
    result = int(input("Введите число от 1 до 100: "))
    if result == number:
        print("Угадал")
        break
    elif result < number:
        print("Введенное число меньше загаданного.")
    elif result > number:
        print("Введенное число больше загаданного.")

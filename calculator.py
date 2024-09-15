# Description - program calculates basic mathematical operations: +,-,*,/
# Input - user enters numbers and operation sign
# Output - calculated number
# Authors: Калинина, Козлова, Субракова, Финк


def calculator():
    # Запрос у пользователя двух чисел
    try:
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
    except ValueError:
        print("Ошибка: необходимо ввести числа через.")
        return

    # Запрос у пользователя операции
    operation = input("Введите операцию (+, -, *, /): ")

    # Выполнение операции
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            print("Ошибка: деление на ноль.")
            return
    else:
        print("Ошибка: неверная операция.")
        return

    # Вывод результата
    print(f"Результат: {result}")

# Запуск калькулятора
calculator()

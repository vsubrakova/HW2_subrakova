# Description - program calculates basic mathematical operations: +,-,*,/
# Input - user enters numbers and operation sign
# Output - calculated number
# Authors: Калинина, Козлова, Субракова, Финк

def divide(a, b):
    if b == 0:
        return "Ошибка! Деление на ноль."
    return a / b

def main():
    expression = input("Введите выражение: ")
    num1, operator, num2 = expression.split()

    num1 = float(num1)
    num2 = float(num2)

    if operator == '/':
        result = divide(num1, num2)

    print(result)

if __name__ == "__main__":
    main()


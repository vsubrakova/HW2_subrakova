# Description - program calculates basic mathematical operations: +,-,*,/
# Input - user enters numbers and operation sign
# Output - calculated number
# Authors: Калинина, Козлова, Субракова, Финк
expression = input("введите выражение, используя пробелы до и после оператора")
expression_split = expression.split()
num1 = float(expression_split[0])  # первое число выражения
operator = expression_split[1]  # оператор выражения
num2 = float(expression_split[2])  # второе число выражения
if operator == "-":  # условие
    result = num1 - num2  
    print(result)

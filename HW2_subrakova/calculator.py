# Description - program calculates basic mathematical operations: +,-,*,/
# Input - user enters numbers and operation sign
# Output - calculated number
# Authors: Калинина, Козлова, Субракова, Финк



def add(x, y):
       return x + y
def multiply(x,y):
       return x*y
def minus(x,y):
       return x-y



def main():
    
    inp = input("Введите выражение, используя пробелы до и после оператора, дробные числа должны быть разделены .")
    string_to_list = inp.split( )
    a = float(string_to_list[0])
    b = float(string_to_list[2])
    operator = string_to_list[1]


if operator == '+':
    result = add(x,y)
elif operator == '*':
    result = multiply(x*y)
elif operator == '-':
    result = minus(x-y)
    


return result
print(main())
    




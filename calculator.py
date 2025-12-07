def addition(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num1 * num2

def division(num1, num2):
    if num2 == 0:
        return "Ошибка: деление на ноль!"
    return num1 / num2


num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))

print("Доступные операции:")
print("1. Сложение (+)")
print("2. Вычитание (-)")
print("3. Умножение (*)")
print("4. Деление (/)")

while True:
    operation = input("Введите символ операции (+, -, *, /): ")

    if operation == '+':
        result = addition(num1, num2)
        print(num1, '+', num2, '=', result)
        break
    if operation == '-':
        result = subtraction(num1, num2)
        print(num1, '-', num2, '=', result)
        break
    if operation == '*':
        result = multiplication(num1, num2)
        print(num1, '*', num2, '=', result)
        break
    if operation == '/':
        result = division(num1, num2)
        print(num1, '/', num2, '=', result)
        break
    if operation not in ['+', '-', '*', '/']:
        print("Ошибка: неверная операция.")
        continue

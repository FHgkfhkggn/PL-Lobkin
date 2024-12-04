def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def calculate_expression(x, n):
    if n == 0:
        return 1
    else:
        return (x ** n) / factorial(n)


x = int(input("Введите натуральное число X: "))
y = int(input("Введите натуральное число Y: "))

result = calculate_expression(x, y)
print(f"Результат выражения {x}^{n}/{n}! равен: {result}")

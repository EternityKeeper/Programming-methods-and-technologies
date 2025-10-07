#normal task 1
def find_min(lst):
    if not lst:
        return None

    min_val = lst[0]
    for num in lst[1:]:
        if num < min_val:
            min_val = num
    return min_val


numbers = [5, -2, 10, 3, -8, 0]
print(find_min(numbers))

#normal task 2

number = int(input("Введите число: "))
print(f"Таблица умножения для числа {number}:")
for i in range(1, 11):
    print(f"{number} × {i} = {number * i}")

#normal task 3

number_a = float(input("Введите первое число: "))
operation = input("Введите операцию (+, -, *, /): ")
number_b = float(input("Введите второе число: "))

if operation == '+':
    result = number_a + number_b
elif operation == '-':
    result = number_a - number_b
elif operation == '*':
    result = number_a * number_b
elif operation == '/':
    if number_b != 0:
        result = number_a / number_b
    else:
        result = "Ошибка: деление на ноль!"
else:
    result = "Ошибка: неизвестная операция!"

print(f"Результат: {number_a} {operation} {number_b} = {result}")
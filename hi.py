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

n = int(input("Введите число: "))
print(f"Таблица умножения для числа {n}:")
for i in range(1, 11):
    print(f"{n} × {i} = {n * i}")

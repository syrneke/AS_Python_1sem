#вар 9
print("ЗАДАЧА А")
try:
    n = int(input("Введите число для факториала: "))
    if n < 0:
        raise ValueError("Отрицательное число")
    f = 1
    for i in range(1, n + 1):
        f = f * i
    print("Факториал:", f)
except ValueError as e:
    print("Ошибка:", e)
  
print("ЗАДАЧА Б")
try:
    n = int(input("Введите число для проверки: "))
    if n <= 0:
        raise ValueError("Число не является положительным")
    print("Число является положительным")
except ValueError as e:
    print("Ошибка:", e)

print("ЗАДАЧА В")
# Задача в
try:
    n = int(input("Введите число для факториала: ")) 
    assert n >= 0, "Отрицательное число"
    f = 1
    for i in range(1, n + 1):
        f = f * i
    print("Факториал:", f)
except AssertionError as e:
    print("Ошибка:", e)

#вар 9
#A
def factorial_with_valueerror():
    """
    Вычисляет факториал числа с обработкой отрицательных чисел через ValueError
    """
    try:
        # Ввод числа от пользователя
        number = int(input("Введите целое число для вычисления факториала: "))
        
        # Проверка на отрицательное число
        if number < 0:
            raise ValueError("Отрицательное число")
        
        # Вычисление факториала
        result = 1
        for i in range(1, number + 1):
            result *= i
        
        # Вывод результата
        print(f"Факториал числа {number} равен: {result}")
        return result
        
    except ValueError as e:
        # Обработка исключения ValueError
        if str(e) == "Отрицательное число":
            print(f"Ошибка: {e}")
        else:
            print("Ошибка: Введено не целое число")
        return None
    except Exception as e:
        # Обработка других исключений
        print(f"Произошла непредвиденная ошибка: {e}")
        return None


# Пример использования функции
print("Задача а): Факториал с исключением ValueError")
print("=" * 50)
factorial_with_valueerror()

#Б
def check_positive_number():
    """
    Проверяет, является ли число положительным, с обработкой исключений
    """
    try:
        # Ввод числа от пользователя
        number = float(input("\nВведите число для проверки: "))
        
        # Проверка на положительное число
        if number <= 0:
            raise ValueError("Число не является положительным")
        
        # Если число положительное
        print(f"Число {number} является положительным")
        return True
        
    except ValueError as e:
        # Обработка исключения ValueError
        if str(e) == "Число не является положительным":
            print(f"Ошибка: {e}")
        else:
            print("Ошибка: Введено не число")
        return False
    except Exception as e:
        # Обработка других исключений
        print(f"Произошла непредвиденная ошибка: {e}")
        return False


# Пример использования функции
print("\n\nЗадача б): Проверка положительного числа")
print("=" * 50)
check_positive_number()

#B
def factorial_with_assert():
    """
    Вычисляет факториал числа с проверкой через assert
    """
    try:
        # Ввод числа от пользователя
        number = int(input("\nВведите целое число для вычисления факториала: "))
        
        # Проверка условия с помощью assert
        # Если условие ложно, будет вызвано исключение AssertionError
        assert number >= 0, "Отрицательное число"
        
        # Вычисление факториала
        result = 1
        for i in range(1, number + 1):
            result *= i
        
        # Вывод результата
        print(f"Факториал числа {number} равен: {result}")
        return result
        
    except AssertionError as e:
        # Обработка исключения AssertionError
        print(f"Ошибка: {e}")
        return None
    except ValueError:
        # Обработка исключения при неверном формате числа
        print("Ошибка: Введено не целое число")
        return None
    except Exception as e:
        # Обработка других исключений
        print(f"Произошла непредвиденная ошибка: {e}")
        return None


# Пример использования функции
print("\n\nЗадача в): Факториал с использованием assert")
print("=" * 50)
factorial_with_assert()

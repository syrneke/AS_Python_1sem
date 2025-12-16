#вар 9
def find_max_abs_odd(filename):
    try:
        with open(filename, 'r') as f:
            # Читаем все числа из файла
            numbers = []
            for line in f:
                for part in line.split():
                    try:
                        numbers.append(float(part))
                    except:
                        continue
            
            if not numbers:
                return None
            
            # Ищем максимум среди нечетных позиций
            max_abs = max(abs(num) for i, num in enumerate(numbers) if (i+1) % 2)
            
            # Находим позицию и исходное значение
            for i, num in enumerate(numbers):
                if (i+1) % 2 and abs(num) == max_abs:
                    return max_abs, i+1, num
    except:
        return None

# Пример использования
result = find_max_abs_odd("numbers.txt")
if result:
    print(f"Максимальный модуль: {result[0]}, позиция: {result[1]}, значение: {result[2]}")

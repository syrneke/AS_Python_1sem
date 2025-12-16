#вар9


def remove_digits_from_file(input_file, output_file=None):
    
    try:
        # Читаем исходный файл
        with open(input_file, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Удаляем цифры
        content_no_digits = ''.join(char for char in content if not char.isdigit())
        
        # Определяем имя выходного файла
        if output_file is None:
            import os
            base_name = os.path.basename(input_file)
            name, ext = os.path.splitext(base_name)
            output_file = f"no_digits_{name}{ext}"
        
        # Записываем результат в новый файл
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(content_no_digits)
        
        print(f"Цифры удалены. Результат сохранен в: {output_file}")
        return output_file
    
    except FileNotFoundError:
        print(f"Ошибка: файл '{input_file}' не найден")
        return None
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return None


def count_characters_in_file(file_path, include_spaces=True, include_newlines=False):
   
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        if not include_spaces:
            content = content.replace(' ', '').replace('\t', '')
        
        if not include_newlines:
            content = content.replace('\n', '').replace('\r', '')
        
        char_count = len(content)
        print(f"Количество символов в файле '{file_path}': {char_count}")
        return char_count
    
    except FileNotFoundError:
        print(f"Ошибка: файл '{file_path}' не найден")
        return 0
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return 0


def count_lines_in_file(file_path):
   
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        
        line_count = len(lines)
        print(f"Количество строк в файле '{file_path}': {line_count}")
        return line_count
    
    except FileNotFoundError:
        print(f"Ошибка: файл '{file_path}' не найден")
        return 0
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return 0


def analyze_file(file_path):
    
    print(f"\nАнализ файла: {file_path}")
    print("=" * 50)
    
    lines = count_lines_in_file(file_path)
    chars_with_spaces = count_characters_in_file(file_path, include_spaces=True, include_newlines=True)
    chars_without_spaces = count_characters_in_file(file_path, include_spaces=False, include_newlines=False)
    
    print(f"\nИтоговая статистика:")
    print(f"Количество строк: {lines}")
    print(f"Количество символов (с пробелами и переносами): {chars_with_spaces}")
    print(f"Количество символов (без пробелов и переносов): {chars_without_spaces}")
    print("=" * 50)


# Пример использования модуля
if __name__ == "__main__":
    # Создадим тестовый файл для демонстрации
    test_content = """Hello World 123!
This is a test file 456.
It contains some text 789
and numbers 0, 1, 2, 3.
Last line without numbers."""
    
    with open("test_file.txt", "w", encoding="utf-8") as f:
        f.write(test_content)
    
    print("Тестирование модуля file_operations.py")
    print("=" * 50)
    
    # Тестируем функции
    analyze_file("test_file.txt")
    
    # Удаляем цифры из файла
    output_file = remove_digits_from_file("test_file.txt")
    
    # Анализируем полученный файл
    if output_file:
        analyze_file(output_file)
    
    # Очистка тестовых файлов (опционально)
    import os
    if os.path.exists("test_file.txt"):
        os.remove("test_file.txt")
    if os.path.exists(output_file):
        os.remove(output_file)


# Импортируем наш модуль
import file_operations

def main():
    print("Программа для работы с текстовыми файлами")
    print("=" * 50)
    
    while True:
        print("\nМеню:")
        print("1. Удалить цифры из файла")
        print("2. Посчитать символы в файле")
        print("3. Посчитать строки в файле")
        print("4. Полный анализ файла")
        print("5. Выйти")
        
        choice = input("\nВыберите действие (1-5): ")
        
        if choice == "1":
            input_file = input("Введите путь к исходному файлу: ")
            output_file = input("Введите путь для выходного файла (или оставьте пустым): ")
            if output_file.strip() == "":
                output_file = None
            
            file_operations.remove_digits_from_file(input_file, output_file)
        
        elif choice == "2":
            file_path = input("Введите путь к файлу: ")
            include_spaces = input("Включать пробелы? (y/n): ").lower() == 'y'
            include_newlines = input("Включать переносы строк? (y/n): ").lower() == 'y'
            
            count = file_operations.count_characters_in_file(
                file_path, 
                include_spaces, 
                include_newlines
            )
            print(f"Результат: {count} символов")
        
        elif choice == "3":
            file_path = input("Введите путь к файлу: ")
            count = file_operations.count_lines_in_file(file_path)
            print(f"Результат: {count} строк")
        
        elif choice == "4":
            file_path = input("Введите путь к файлу: ")
            file_operations.analyze_file(file_path)
        
        elif choice == "5":
            print("Выход из программы")
            break
        
        else:
            print("Неверный выбор. Попробуйте еще раз.")

#вар9
def center_text_simple(input_file, output_file, width=50):
    """Компактная версия функции центрирования текста"""
    try:
        with open(input_file, 'r', encoding='utf-8') as infile:
            lines = infile.readlines()
        
        with open(output_file, 'w', encoding='utf-8') as outfile:
            for line in lines:
                line = line.rstrip('\n\r')
                if line.strip():  # Если строка не пустая
                    # Добавляем пробел для строк нечетной длины
                    if len(line) % 2: line = ' ' + line
                    # Центрируем
                    spaces = max(0, width - len(line))
                    outfile.write(' ' * (spaces // 2) + line + '\n')
                else:  # Пустая строка
                    outfile.write('\n')
        return True
    except Exception as e:
        print(f"Ошибка: {e}")
        return False


if __name__ == "__main__":
    # Быстрый тест
    test_lines = [
        "Короткая",
        "Строка средней длины",
        "Очень длинная строка, которая должна быть обработана правильно",
        "",
        "Еще одна строка"
    ]
    
    # Записываем тестовые данные
    with open("test_input.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(test_lines))
    
    # Обрабатываем
    center_text_simple("test_input.txt", "test_output.txt", 50)
    
    # Читаем результат
    print("Результат центрирования:")
    with open("test_output.txt", "r", encoding="utf-8") as f:
        for i, line in enumerate(f, 1):
            line = line.rstrip('\n')
            # Показываем пробелы
            vis_line = line.replace(' ', '·')
            print(f"{i:2}: |{vis_line}| (длина: {len(line)})")

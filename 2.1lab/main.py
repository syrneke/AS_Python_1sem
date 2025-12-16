#вар9

def task_a(dictionary):
    """Перебирает все ключи и значения в словаре"""
    print("Задача а):")
    for key, value in dictionary.items():
        print(f"key: {key}, value: {value}")

def task_b(list_of_dicts, target_key):
    """Вычисляет сумму значений по определенному ключу в списке словарей"""
    print("\nЗадача б):")
    total = 0
    for item in list_of_dicts:
        if target_key in item:
            total += item[target_key]
    return total

def task_c(students_dict):
    """Фильтрует данные, оставляя только рост учащихся"""
    print("\nЗадача в):")
    filtered_dict = {}
    for name, data in students_dict.items():
        filtered_dict[name] = {'рост': data['рост']}
    return filtered_dict

# Примеры использования
if __name__ == "__main__":
    # Задача а)
    sample_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    task_a(sample_dict)
    
    # Задача б)
    list_dicts = [{'a': 1}, {'a': 2}, {'a': 3}, {'b': 1}]
    key_to_sum = 'a'
    result_b = task_b(list_dicts, key_to_sum)
    print(f"Сумма значений по ключу '{key_to_sum}': {result_b}")
    
    # Задача в)
    students = {
        'Иван': {'рост': 170, 'вес': 70},
        'Михаил': {'рост': 180, 'вес': 75},
        'Анна': {'рост': 165, 'вес': 60}
    }
    result_c = task_c(students)
    print("Отфильтрованные данные (только рост):")
    for name, data in result_c.items():
        print(f"{name}: {data}")

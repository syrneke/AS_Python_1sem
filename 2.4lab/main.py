#вар9
# а) Функция capitalize_words
def capitalize_words(text, separator=' '):
    
    words = text.split(separator)
    return separator.join(word.capitalize() for word in words)

# б) Функция filter_elements
def filter_elements(list1, list2, filter_function=None):
   
    combined = list1 + list2
    if filter_function is None:
        return combined
    return [x for x in combined if filter_function(x)]

# в) Функция merge_dictionaries
def merge_dictionaries(*dicts):
    
    result = {}
    for d in dicts:
        result.update(d)
    return result

# г) Функция unique_keys
def unique_keys(*dicts):
    
    from collections import Counter
    
    # Считаем сколько раз встречается каждый ключ
    key_counter = Counter()
    for d in dicts:
        key_counter.update(d.keys())
    
    # Собираем значения для ключей, которые встречаются 1 раз
    result = {}
    for d in dicts:
        for key, value in d.items():
            if key_counter[key] == 1:
                result[key] = value
    
    return result

# Тестирование всех функций
if __name__ == "__main__":
    print("а) capitalize_words:")
    print(f"   capitalize_words('hello world') → {capitalize_words('hello world')}")
    print(f"   capitalize_words('python,java,c++', separator=',') → {capitalize_words('python,java,c++', separator=',')}")
    
    print("\nб) filter_elements:")
    print(f"   filter_elements([1, 2, 3], [4, 5, 6]) → {filter_elements([1, 2, 3], [4, 5, 6])}")
    print(f"   filter_elements([1, 2, 3], [4, 5, 6], filter_function=lambda x: x > 3) → {filter_elements([1, 2, 3], [4, 5, 6], filter_function=lambda x: x > 3)}")
    print(f"   filter_elements([1, 2, 3], [4, 5, 6], filter_function=lambda x: x % 2 == 0) → {filter_elements([1, 2, 3], [4, 5, 6], filter_function=lambda x: x % 2 == 0)}")
    
    print("\nв) merge_dictionaries:")
    print(f"   merge_dictionaries({{'a': 1}}, {{'b': 2}}, {{'a': 3}}) → {merge_dictionaries({'a': 1}, {'b': 2}, {'a': 3})}")
    print(f"   merge_dictionaries({{'x': 5}}, {{'y': 6}}, {{'z': 7}}, {{'x': 8}}) → {merge_dictionaries({'x': 5}, {'y': 6}, {'z': 7}, {'x': 8})}")
    
    print("\nг) unique_keys:")
    print(f"   unique_keys({{'a': 1, 'b': 2}}, {{'b': 3, 'c': 4}}) → {unique_keys({'a': 1, 'b': 2}, {'b': 3, 'c': 4})}")
    print(f"   unique_keys({{'x': 5}}, {{'y': 6}}, {{'z': 7}}, {{'x': 8}}) → {unique_keys({'x': 5}, {'y': 6}, {'z': 7}, {'x': 8})}")
    print(f"   unique_keys({{'a': 1}}, {{'a': 2}}, {{'b': 3}}) → {unique_keys({'a': 1}, {'a': 2}, {'b': 3})}")

#вар9
def increase_even_numbers(numbers, increment):
    has_even = any (num % 2 == 0 for num in numbers)
    if has_even:
        result = [num + increment if num % 2 == 0 else num for num in numbers]
        return result
    else:
        return numbers
numbers = [1,2,3,4,5,6,7,8,9]
increment=10
result= increase_even_numbers(numbers,increment)
print(f"Исходный список: {numbers}")
print(f"Полсде увеличения четных чисел на {increment}: {result}")

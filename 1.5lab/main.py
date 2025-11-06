#вар9
def filter_and_sort(numbers):
    result = sorted([num for num in numbers if num < 15], reverse = True)
    return result
numbers = [20,5,12,18,3,10,25,8,14,23,4,1,9,16]
result = filter_and_sort(numbers)
print(f"Исходный список: {numbers}")
print(f"Числа < 15 по убыванию: {result}")

    

#вар9
#ЗАДАЧАA 
dict1 = {'a':1, 'b':2, 'c':3, 'd':4}
print("Задача А")
for k in dict1:
    v = dict1[k]
    print(f"key: {k}, value: {v}")

#ЗАДАЧАБ 
list1 = [{'a': 1}, {'a': 2}, {'a': 3}, {'b': 1}]
print("Задача Б")
s = 0 
for d in list1:
    if 'a' in d:
        s = s + d['a']
print(f"Сумма: {s}")

#ЗАДАЧАВ
students = {'Иван': {'рост':170, 'вес':70}, 'Михаил': {'рост':180, 'вес':75}}
print("Задача В")
new_dict = {}
for name in students:
    height_dict = {'рост': students[name]['рост']}
    new_dict[name] = height_dict
print(f"Результат: {new_dict}")

#Задание 5 из ЕГЭ профильная математика [https://math-ege.sdamgia.ru/problem?id=509352]
#Какова вероятность того, что случайно выбранный телефонный номер оканчивается двумя чётными цифрами?

count=0
for i in range(10):
    if i % 2 == 0:
        count+=1
print(f"колво четных цифр: {count}")
prob_single=count/10

prob_double=prob_single* prob_single

print(f"вероятность: {count}")
    

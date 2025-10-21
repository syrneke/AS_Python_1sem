#9вар даны два целых числа А и В(А<В) найти сумму квадратов всех целых чисел от А до В включительно
A = 2
B = 5
sum_square = 0
for numbers in range(A,B+1):
  square = number * number
  sum_2 += square
  print(f"{number}**2 = {square}")

print(f"сумма квадратов  от {A} до {B}: {sum_square}")

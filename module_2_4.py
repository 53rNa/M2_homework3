# Задача "Всё не так уж просто"

# Проверка чисел данных из списка на простые и непростые
# Простое число — натуральное (целое положительное) число,
# имеющее ровно два различных натуральных делителя — единицу и самого себя.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for i in range(1,len(numbers)):
    count = 0
    for j in range(2, int(numbers[i] ** 0.5) + 1):      # Проходим по циклу до корня числа, если не находим делитель
        if numbers[i] % j == 0:                         # до корня данного числа,то дальше нет смысла искать,
            count += 1                                  # не найдём делители.
            not_primes.append(numbers[i])               # Формируем список непростых чисел
            break
    if count == 0:
        primes.append(numbers[i])                       # Формируем список простых чисел

print('Primes:', primes)                                # Вывод обоих списков в консоль
print ('Not_Primes:', not_primes)

# Второй вариант

# for i in range(1,len(numbers)):
#     count = 0
#     for j in range(1, numbers[i]):
#         if numbers[i] % j == 0 and numbers[i] != j and j != 1:    # Поиск делителей числа
#             count += 1
#             print ('Not_Primes:', numbers[i])
#             not_primes.append(numbers[i])
#             break
#     if count == 0:                                                # Не нашли ни одного делителя
#         print ('Primes:',numbers[i])
#         primes.append(numbers[i])
#
# print ('Primes:', primes)
# print ('Not_Primes:', not_primes)



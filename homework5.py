import random
random_numbers = [random.randint(1, 100) for _ in range(10)]
print("Генеруємий список:", random_numbers)
largest_number = random_numbers[0]
index = 1
while index < len(random_numbers):
    if random_numbers[index] > largest_number:
        largest_number = random_numbers[index]
    index += 1
print("Найбільше число:", largest_number)


import random
list1 = [random.randint(1, 10) for _ in range(10)]
list2 = [random.randint(1, 10) for _ in range(10)]
print("Список 1:", list1)
print("Список 2:", list2)
common_list = []
index1 = 0
while index1 < len(list1):
    index2 = 0
    while index2 < len(list2):
        if list1[index1] == list2[index2] and list1[index1] not in common_list:
            common_list.append(list1[index1])
        index2 += 1
    index1 += 1
print("Цілі числа без дублікатів:", common_list)



all_numbers = list(range(1, 101))
filtered_numbers = []
index = 0
while index < len(all_numbers):
    current_number = all_numbers[index]

    if current_number % 7 == 0 and current_number % 5 != 0:
        filtered_numbers.append(current_number)

    index += 1
print("Числа, які діляться на 7, але не кратні 5:", filtered_numbers)

#1
def count_word_occurrences(sentence):
    words = sentence.split()
    word_occurrences = {}

    for word in words:
        word = word.strip('.,!?').lower()

        if word in word_occurrences:
            word_occurrences[word] += 1
        else:
            word_occurrences[word] = 1

    return word_occurrences

input_sentence = input("Введіть речення: ")

result_dict = count_word_occurrences(input_sentence)

print("Вивід результату:", result_dict)

#2
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

total_prices = {}

for item in stock:
    total_prices[item] = stock[item] * prices[item]

print("Загальна вартість:", total_prices)

#3
result_list = [(i, i**2) for i in range(1, 11)]
print(result_list)

#4
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

day_to_number = {i + 1: day for i, day in enumerate(days_of_week)}

number_to_day = {day: i + 1 for i, day in enumerate(days_of_week)}

print("Список днів тижня:", days_of_week)
print("Словник:", day_to_number)
print("Зворотний словник:", number_to_day)

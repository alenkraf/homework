#1
def example_function():
    a = 13
    b = "Hello"
    c = [9, 8, 7]
    d = {"ім'я": "Oleh", "вік": 48}

    local_variables_count = len(locals())

    print("Локальні змінні функції:", locals())
    print("Кількість локальних змінних:", local_variables_count)

# Виклик функції
example_function()

#2
def outer_function(message):
    # Внутрішня функція повертається зовнішньою
    def inner_function():
        print(f"Повідомлення з внутрішньої функції: {message}")

    # Повернення внутрішньої функції
    return inner_function

# Виклик зовнішньої функції з повідомленням
result_function = outer_function("Я в середині внутрішньої функції!")

# Виклик повернутої функції
result_function()

#3
def choose_func(nums: list, func1, func2):
    if all(num > 0 for num in nums):
        return func1(nums)
    else:
        return func2(nums)

nums1 = [1, -2, 3, 4, 5]
nums2 = [3, 5, 7, 9, 15]

def square_nums(nums):
    return [num ** 2 for num in nums]

def remove_negatives(nums):
    return [num for num in nums if num > 0]

result1 = choose_func(nums1, square_nums, remove_negatives)
result2 = choose_func(nums2, square_nums, remove_negatives)

print(result1)
print(result2)
print("Test cases passed successfully.")


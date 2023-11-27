#1
def oops():
    # Створюємо помилку IndexError
    raise IndexError("Упс! Помилка IndexError")

def handle_error():
    try:
        # Виклик функції УПС через try 
        oops()
    except IndexError as e:
        # Вловлюємо помилку IndexError
        print(f"Виникла помилка: {e}")
    except KeyError as e:
        # Вловлюємо помилку KeyError (не буде задіяно, якщо УПС має IndexError)
        print(f"Виникла помилка: {e}")
    else:
        # Виконується, якщо маємо виключення
        print("Помилка відсутня.")

# Тестування функції handle_error
handle_error()


def oops():
    # Створюємо KeyError замість IndexError
    raise KeyError("Упс! Помилка KeyError")

# Тестування функції handle_error з допомогою УПС, що викликає KeyError
handle_error()



#2
def calculate_squared_divided_by_b():
    try:
        # Ввести два числа
        a = float(input("Введіть значення для a: "))
        b = float(input("Введіть значення для b: "))
        
        # Обчислити квадрат a, поділений на b
        result = (a ** 2) / b

        # Повернути результат
        return result

    except ValueError:
        # Опрацювання інформації, коли вхідні дані не числа
        print("Помилка. Введіть числа")
        # Повторна спроба виклику функції
        return calculate_squared_divided_by_b()

    except ZeroDivisionError:
        # Якщо b дорівнює нулю (ділення на нуль)
        print("Помилка. Ділення на нуль неможливе. Введіть b не рівне нулю")
        # Повторна спроба виклику функції
        return calculate_squared_divided_by_b()

    except Exception as e:
        # Обробка інших випадків
        print(f"An unexpected error occurred: {e}")
        # Повторна спроба виклику функції
        return calculate_squared_divided_by_b()

# Тест функції
result = calculate_squared_divided_by_b()

# Вивід результату, якщо він доступний
if result is not None:
    print(f"Результат a в квадраті ділене на b: {result}")

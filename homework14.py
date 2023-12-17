# #Task1 School
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def get_details(self):
#         return f"Ім'я: {self.name}, Вік: {self.age}"

# class Student(Person):
#     def __init__(self, name, age, student_id):
#         super().__init__(name, age)
#         self.student_id = student_id
#         self.grades = {}

#     def add_grade(self, subject, grade):
#         self.grades[subject] = grade

#     def get_grades(self):
#         return self.grades

# class Teacher(Person):
#     def __init__(self, name, age, employee_id, salary):
#         super().__init__(name, age)
#         self.employee_id = employee_id
#         self.salary = salary
#         self.subjects_taught = []

#     def assign_subject(self, subject):
#         self.subjects_taught.append(subject)

#     def get_salary(self):
#         return f"Зарплатня: {self.salary}"

#     def get_subjects_taught(self):
#         return self.subjects_taught


# student1 = Student("Олеся", 17, "S12345")
# student1.add_grade("Математика", 70)
# student1.add_grade("Історія", 90)

# teacher1 = Teacher("Олександр Попов", 45, "T98765", 50000)
# teacher1.assign_subject("Математика")
# teacher1.assign_subject("Історія")

# print(student1.get_details())
# print(f"Оцінки: {student1.get_grades()}")

# print(teacher1.get_details())
# print(teacher1.get_salary())
# print(f"Які викладає предмети: {teacher1.get_subjects_taught()}")

#Task2 Mathematician
class Mathematician:

    def square_nums(self, your_list : list):
        return [num ** 2 for num in your_list]
    
    def remove_positives(self, your_list : list):
        return [num for num in your_list if num < 0]
    
    def filter_leaps(self, your_list : list):
        return [num for num in your_list if num % 400 == 0 or (num % 4 == 0 and num % 100 != 0)]

m = Mathematician()
assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]
assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]
assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]


#Task 3 Product Store
class Product:
    def __init__(self, type_, name, price):
        self.type_ = type_
        self.name = name
        self.price = price

class ProductStore:
    def __init__(self):
        self.products = []
        self.income = 0

    def add(self, product, amount):
        self.products.append(dict(type_=product.type_, name=product.name, price=product.price * 1.3, amount=amount))
    
    def set_discount(self, identifier, percent, identifier_type="type_"):
        for product in self.products:
            if product[identifier_type] == identifier:
                product["price"] *= (100 - percent) / 100
    
    def sell_product(self, product_name, amount):
        for product in self.products:
            if product["name"] == product_name:
                if product["amount"] >= amount:
                    product["amount"] -= amount
                    self.income += amount * product["price"]
                else:
                    raise ValueError("Insufficient quantity of the selected product")
    
    def get_income(self):
        return self.income
    
    def get_all_products(self):
        return self.products
    
    def get_product_info(self, product_name):
        for product in self.products:
            if product["name"] == product_name:
                return tuple([product["name"], product["amount"]])

p = Product("Sport", "Football T-Shirt", 100)
p2 = Product("Food", "Ramen", 1.5)
s = ProductStore()

s.add(p, 10)
s.add(p2, 300)
s.sell_product("Ramen", 10)
assert s.get_product_info("Ramen") == ("Ramen", 290)

#Task4 
class CustomException(Exception):
    def __init__(self, msg):
        super().__init__(msg)
        self.log_error(msg)

    def log_error(self, msg):
        with open('logs.txt', 'a') as log_file:
            log_file.write(f"Error: {msg}\n")
try:
    # Викликати спеціальний виняток за допомогою повідомлення
    raise CustomException("Це повідомлення про помилку")
except CustomException as e:
    print(f"Перехоплено виняток: {e}")


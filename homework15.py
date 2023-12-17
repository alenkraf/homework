# Task1 Method overloading
class Animal:
    def talk(self):
        pass

class Dog(Animal):
    def talk(self):
        return 'Woof woof'

class Cat(Animal):
    def talk(self):
        return 'Meow'

def perform_talk(animal_instance):
    if not isinstance(animal_instance, Animal):
        raise ValueError("Input must be an instance of Animal class or its subclasses")

    print(animal_instance.talk())
dog_instance = Dog()
cat_instance = Cat()

perform_talk(dog_instance)  # Output: Woof woof
perform_talk(cat_instance)  # Output: Meow

#Task2 Library
class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.authors = []

    def new_book(self, name, year, author):
        book = Book(name, year, author)
        self.books.append(book)
        return book

    def group_by_author(self, author):
        return [book for book in self.books if book.author == author]

    def group_by_year(self, year):
        return [book for book in self.books if book.year == year]

    def __str__(self):
        return f"Library: {self.name}"

    def __repr__(self):
        return f"Library(name='{self.name}')"


class Book:
    total_books = 0

    def __init__(self, name, year, author):
        self.name = name
        self.year = year
        self.author = author
        self.author.books.append(self)
        Book.total_books += 1

    def __str__(self):
        return f"Book: {self.name} ({self.year}) by {self.author.name}"

    def __repr__(self):
        return f"Book(name='{self.name}', year={self.year}, author={repr(self.author)})"


class Author:
    def __init__(self, name, country, birthday):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = []

    def __str__(self):
        return f"Author: {self.name}"

    def __repr__(self):
        return f"Author(name='{self.name}', country='{self.country}', birthday='{self.birthday}')"

library = Library("My Library")

author1 = Author("Alexandre Dumas", "France", "1802-07-24")
author2 = Author("Arthur Conan Doyle", "Scotland", "1859-05-22")

book1 = library.new_book("The Count of Monte Cristo", 1844, author1)
book2 = library.new_book("The Three Musketeers", 1844, author1)
book3 = library.new_book("The Hound of the Baskervilles", 1902, author2)

print(book1)
print(book2)
print(book3)

books_by_author1 = library.group_by_author(author1)
print(f"Books by {author1.name}: {books_by_author1}")

books_by_year_1844 = library.group_by_year(1844)
print(f"Books from the year 1844: {books_by_year_1844}")

print(f"Total books created: {Book.total_books}")

#Task 3 Fraction
from math import gcd

class Fraction:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero.")
        common = gcd(numerator, denominator)
        self.numerator = numerator // common
        self.denominator = denominator // common

    def __add__(self, other):
        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __sub__(self, other):
        new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __mul__(self, other):
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __truediv__(self, other):
        if other.numerator == 0:
            raise ValueError("Cannot divide by zero.")
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        return Fraction(new_numerator, new_denominator)

    def __eq__(self, other):
        return self.numerator == other.numerator and self.denominator == other.denominator

    def __lt__(self, other):
        return self.numerator * other.denominator < other.numerator * self.denominator

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

if __name__ == "__main__":
    x = Fraction(1, 2)
    y = Fraction(1, 4)

    result_addition = x + y
    print(result_addition)  # Output: 3/4

    result_subtraction = x - y
    print(result_subtraction)  # Output: 1/4

    result_multiplication = x * y
    print(result_multiplication)  # Output: 1/8

    result_division = x / y
    print(result_division)  # Output: 2/1

    print(x == Fraction(1, 2))  # Output: True

    print(x < y)  # Output: False


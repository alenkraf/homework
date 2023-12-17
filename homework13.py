#Task1
class Person:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def talk(self):
        print(f"Hello, my name is {self.firstname} {self.lastname} and I'm {self.age} years old.")

person1 = Person("Oleh", "Poryvaiev", 48)
person1.talk()


#Task2
class Dog:
    age_factor = 7

    def __init__(self, dog_age):
        self.dog_age = dog_age

    def human_age(self):
        return self.dog_age * Dog.age_factor

dog1 = Dog(5)
print(f"Собаці {dog1.dog_age} років в собачих роках.")
print(f"В людських роках, собаці приблизно {dog1.human_age()} років.")


#Task3
CHANNELS = ["BBC", "Discovery", "TV1000"]

class TVController:
    def __init__(self, channels):
        self.channels = channels
        self.current_channel_index = 0

    def first_channel(self):
        self.current_channel_index = 0
        return self.current_channel()

    def last_channel(self):
        self.current_channel_index = len(self.channels) - 1
        return self.current_channel()

    def turn_channel(self, n):
        if 1 <= n <= len(self.channels):
            self.current_channel_index = n - 1
        return self.current_channel()

    def next_channel(self):
        self.current_channel_index = (self.current_channel_index + 1) % len(self.channels)
        return self.current_channel()

    def previous_channel(self):
        self.current_channel_index = (self.current_channel_index - 1) % len(self.channels)
        return self.current_channel()

    def current_channel(self):
        return self.channels[self.current_channel_index]

    def exists(self, n_or_name):
        if isinstance(n_or_name, int):
            return "Yes" if 1 <= n_or_name <= len(self.channels) else "No"
        elif isinstance(n_or_name, str):
            return "Yes" if n_or_name in self.channels else "No"

controller = TVController(CHANNELS)

print(controller.first_channel())  # Output: "BBC"
print(controller.last_channel())   # Output: "TV1000"
print(controller.turn_channel(1))  # Output: "BBC"
print(controller.next_channel())   # Output: "Discovery"
print(controller.previous_channel())  # Output: "BBC"
print(controller.current_channel())  # Output: "BBC"
print(controller.exists(4))         # Output: "No"
print(controller.exists("BBC"))     # Output: "Yes"

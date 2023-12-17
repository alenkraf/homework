#Task 1
import re

class EmailDescriptor:

    def __get__(self, obj, objtype=None):
        return obj._email
    
    def __set__(self, obj, value):
        if self.validate_email(value):
            obj._email = value
        else:
            print("Invalid email address")
            obj._email = None

    def validate_email(self, email):
        email_pattern = re.compile(
            r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        )
        return bool(re.match(email_pattern, email))

class Checker:

    email = EmailDescriptor()

    def __init__(self, email):
        self.email = email

checker1 = Checker("username@company.com")
print(checker1.email)  # Output: username@company.com

checker2 = Checker("invalid_email")
print(checker2.email)  # Output: Invalid email address



# Task2
class Boss:
    def __init__(self, id_: int, name: str, company: str):
        self.id = id_
        self.name = name
        self.company = company
        self._workers = []

    def add_worker(self, worker):
        if isinstance(worker, Worker):
            self._workers.append(worker)
        else:
            raise ValueError("Only instances of Worker can be added as workers.")

    @property
    def workers(self):
        return self._workers

    def __str__(self):
        return f"Boss {self.name} ({self.company})"


class Worker:
    def __init__(self, id_: int, name: str, company: str, boss: Boss):
        self.id = id_
        self.name = name
        self.company = company
        self._boss = None
        self.boss = boss

    @property
    def boss(self):
        return self._boss

    @boss.setter
    def boss(self, new_boss):
        if isinstance(new_boss, Boss):
            if self._boss:
                self._boss.workers.remove(self)
            self._boss = new_boss
            new_boss.add_worker(self)
        else:
            raise ValueError("Boss must be an instance of Boss class.")

    def __str__(self):
        return f"Worker {self.name} ({self.company}) assigned to {self.boss}"

# Example usage
boss1 = Boss(1, "Oleksandr Baranchuk", "Ukrtelecom")
worker1 = Worker(101, "Viktor Arap", "Ukrtelecom", boss1)

boss2 = Boss(2, "Vitalii Stoliarov", "NDT")
worker1.boss = boss2

print(worker1)
boss1.add_worker(worker1)
print(boss1)
print(worker1.boss)



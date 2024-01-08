#Task1
def with_index(iterable, start=0):
    n = start
    for elem in iterable:
        yield n, elem
        n += 1

my_str = "qaswedfr"
for i, el in with_index(my_str):
    print(i, " : ", el)


#Task2
def in_range(start, end, step=1):
    current = start
    while (step > 0 and current < end) or (step < 0 and current > end):
        yield current
        current += step
for i in in_range(0, 10, 2):
    print(i)


#Task3
class MyIterable:

    def __init__(self, data) -> None:
        self.data = data
    
    def __iter__(self):
        self.i = 0
        return self
    
    def __next__(self):
        if self.i < len(self.data):
            result = self.data[self.i]
            self.i += 1
            return result
        else:
            raise StopIteration

    def __getitem__(self, key):
        return self.data[key]

counter = MyIterable([1, 2, 3, 4, 5])

for i in counter:
    print(i)

print(counter[0])


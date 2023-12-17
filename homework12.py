#Task1
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"{func.__name__} called with {args}, {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@logger
def add(x, y):
    return x + y

@logger
def square_all(*args):
    return [arg ** 2 for arg in args]

result_add = add(4, 5)
result_square_all = square_all(2, 3, 4)


#Task2
def stop_words(words: list):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            for word in words:
                result = result.replace(word, "*")
            return result
        return wrapper
    return decorator

@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"
print(create_slogan("Atolic"))
assert create_slogan("Steve") == "Steve drinks * in his brand new *!"


#Task3
def arg_rules(type_: type, max_length: int, contains: list):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for arg in args:
                # Check type
                if not isinstance(arg, type_):
                    print(f"Error: Argument type should be {type_}")
                    return False

                # Check max length
                if isinstance(arg, str) and len(arg) > max_length:
                    print(f"Error: Argument length exceeds the maximum length of {max_length}")
                    return False

                # Check contains
                if contains and any(symbol not in arg for symbol in contains):
                    print(f"Error: Argument should contain symbols {contains}")
                    return False

            return func(*args, **kwargs)
        return wrapper
    return decorator

@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


assert create_slogan('johndoe05@gmail.com') is False
assert create_slogan('05years') is False
assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'

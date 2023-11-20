#1
def favorite_movie(movie_name):
    print(f"My favorite movie is named {movie_name}")

favorite_movie("The Shawshank Redemption")

#2
def make_country(country_name, country_capital):
    country_info = {'name': country_name, 'capital': country_capital}
    print(country_info)

make_country('Ukraine', 'Kyiv')

#3
x=5
y=4
z=3
def make_operation(operator, *args):
    if operator not in ('+', '-', '*'):
        return "Невірний оператор"

    result = args[0]

    if operator == '+':
        for num in args[1:]:
            result += num
    elif operator == '-':
        for num in args[1:]:
            result -= num
    elif operator == '*':
        for num in args[1:]:
            result *= num

    return result

print(make_operation('+', x, y, z))
print(make_operation('-', x, y, z))
print(make_operation('*', x, y, z))
my_list = [
    1, 3, 6, 11,
    4, 2, 4, 9,
    17, 16, 0,
]

new_list = []

for element in my_list:
        new_list.append('even' if element % 2 == 0 else 'odd')

def odd_or_even(number):
    return 'even' if number % 2 == 0 else 'odd'

result = [ odd_or_even(number)
           for number in my_list ]

print(result)


print(new_list)
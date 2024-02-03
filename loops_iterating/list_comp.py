squares = [ number * number for number in range(5) ]
print(squares)

mult_of_6 = [ num for num in range(20) if num % 6 == 0 ]
print(mult_of_6)

even_squares = [ n * n for n in range(10) if n % 2 == 0 ]
print(even_squares)

cats_colors = {
    'Tess':   'brown',
    'Leo':    'orange',
    'Fluffy': 'gray',
    'Ben':    'black',
    'Kat':    'orange',
}
names = [ name.upper()
          for name in cats_colors
          if cats_colors[name] == 'orange'
          if name[0] == 'L' ]
print(names)
def number_range(num):
    if num >= 0 and num < 51:
        print(f'{num} is between 0 and 50')
    elif num > 51 and num < 101:
        print(f'{num} is between 51 and 100')
    elif num < 0:
        print(f'{num} is less than 0')
    else:
        print(f'{num} is greater than 100')


number_range(0)     # 0 is between 0 and 50
number_range(25)    # 25 is between 0 and 50
number_range(50)    # 50 is between 0 and 50
number_range(75)    # 75 is between 51 and 100
number_range(100)   # 100 is between 51 and 100
number_range(101)   # 101 is greater than 100
number_range(-1)    # -1 is less than 0
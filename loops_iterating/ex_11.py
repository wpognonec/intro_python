my_list = [
  [1, 3, 6, 11],
  [4, 2, 4],
  [9, 17, 16, 0],
]

x = 0
while x < len(my_list):
    y = 0
    while y < len(my_list[x]):
        if my_list[x][y] % 2 == 0:
            print(my_list[x][y])
        y += 1
    x += 1
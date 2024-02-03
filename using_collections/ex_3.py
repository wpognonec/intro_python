t1 = (1, 2, 3, 4, 5)
t2 = list(reversed(t1))
t2.pop(0)
t2.pop()
t2 = tuple(t2)
print(t2)

print(t1[3:0:-1])
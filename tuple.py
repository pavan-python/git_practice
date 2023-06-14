#create tuple

my_tuple = ('python', 'van', 1991, 3.12)
print([my_tuple[2]])
print(my_tuple.count('van'))
print(my_tuple.index(3.12))




for i in my_tuple:
    print(i)

for i in range(len(my_tuple)):
    print(f'index: {i}, item: {my_tuple[i]}')
import os

path = os.path.abspath(os.path.join('example.txt'))
path2 = os.path.abspath(os.path.join('example.txt', os.pardir))
# print(os.path.exists(path))
# print(os.path.exists(path2))


print(os.path.isdir(path2))
print(os.path.isdir('tools'))

print(os.path.isfile(os.path.abspath(os.path.join('tools', 'algoithm_time.txt'))))

print(os.path.abspath('tools'))
print(os.path.abspath('..'))
print(os.path.abspath(''))
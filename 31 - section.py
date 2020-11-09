import os

my_path = os.path.join(os.getcwd(), 'myfile.txt')
directory_path = os.path.dirname(my_path)
file_path = os.path.basename(my_path)
# print(my_path)
# print(directory_path)
# print(file_path)


print(os.path.split(my_path))
print(os.path.splitext(my_path))
# input
# output
# I/O Stream

filename = 'text.csv'

"""
with open(filename, 'r') as myfile:
    # this method makes a list
    # where each line of the file is on 
    # element in the list
    lines = myfile.readlines()
"""
"""
with open(filename, 'r') as myfile:
    # this method makes a list
    # where each line of the file is on 
    # element in the list
    content = myfile.read()
    lines = content.split("\n")
"""
# Performance
# Comprehension
with open(filename, 'r') as myfile:
    lines = [line.strip() for line in myfile]

print(lines)


with open('text.csv') as input_file, open('myfile.txt', 'w') as output_file:
    for line in input_file:
        output_file.write(line + '\n')


class File():
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
    
    def __enter__(self):
        self.open_file = open(self.filename, self.mode)
        return self.open_file
    
    def __exit__(self, *args):
        self.open_file.close()

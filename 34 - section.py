



filename = 'text.csv'
fileobj = open(filename, 'r')
fileobj.seek(7)
pos = fileobj.tell()
print("we are at {}".format(pos))
fileobj.close()
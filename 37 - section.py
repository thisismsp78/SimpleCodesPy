import os

fname = 'myfile5.txt'

def create_file(fname, unicode = True):
    if not os.path.isfile(fname):
        if unicode:
            with open(fname, 'w', encoding = 'utf-8') as myfile:
                myfile.write("Line1\n")
                myfile.write("Line2\n")
                myfile.write("Line3\n")
                myfile.write("سپهر")

        with open(fname, 'w', encoding = 'utf-8') as myfile:
                myfile.write("Line1\n")
                myfile.write("Line2\n")
                myfile.write("Line3\n")
                myfile.write("سپهر")
    else:
        raise IOError("the file with this name: {} , is exist.".format(fname))


create_file(fname)
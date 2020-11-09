# IO Stream
filename = 'text.csv'
with open(filename, 'r') as myfile:
    pass


# Mode
# r --> reading mode.
# w --> writing mode. overwrite
# a --> append  mode.
# ------------------------------
# rb --> reading mode as binary.
# wb --> writing mode as binary.
# ab --> append  mode as binary.
# ------------------------------
# r+ --> read and write.
# w+ --> write and read.
# a+ --> append and read.
# ------------------------------
# rb+ --> read and write mode as binary.
# wb+ --> write and read mode as binary.
# ab+ --> append and read mode as binary.
# ------------------------------
# ##############################
#           PYTHON 3
# ##############################
# x   --> open for exclusive creation, will raise FileExistsError if the file already exist.
# x+  --> read and write if the file does not exist.
# xb  --> open for exclusive creation writing mode as binary.
# xb+ --> read and write like mode as binary.

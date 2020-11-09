# input

def input_number(msg, err_msg = None, is_float = False):
    while True:
        try:
            num = input(msg)
            if num == 'q' or num == 'quit' or num == 'exit':
                exit()
            if is_float:
                return float(num)
            return int(num)

        except ValueError:
            if err_msg is not None:
                print(err_msg)
            else:
                print("Error!")

#Regex


# str
number = input_number("enter number: ", "please input a number", True)
number += 1

print(number)

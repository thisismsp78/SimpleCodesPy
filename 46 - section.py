#Infinite generator

def integers_starting_from(n):
    while True:
        yield n
        n += 1


natural_numbers = integers_starting_from(10)
comp_natural_numbers = (x for x in integers_starting_from(100))

for i in range(100):
    print(next(comp_natural_numbers))


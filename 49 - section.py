def even_the_odds(odd):
    if odd % 2 != 1:
        raise ValueError("Did not get an odd num")
    return odd + 1


f1 = even_the_odds(1)
print(f1)

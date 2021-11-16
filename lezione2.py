the_list = [1, 2, 3, 4, 5, 6]
def sum_list(the_list):
    somma = 0
    for item in the_list:
        somma = somma + item
    return somma

print ('La somma della lista è {}' .format(sum_list(the_list)))
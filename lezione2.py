the_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
def sum_list(the_list):
    somma = 0
    for item in the_list:
        somma = somma + item
    return somma
print ('La somma della lista è {}' .format(sum_list(the_list)))
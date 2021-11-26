#inizializzo un array dove inserire i valori che trovo
values = []
somma = 0
#apro il file
my_file = open ('shampoo_sales.csv', 'r')
for line in my_file:
#divido gli elementi in base a dov'è la virgola
    elements = line.split(',')
#se la riga non è Date, allora mi salvo il valore in value
    if elements[0] != 'Date':
        value = float(elements[1])
        values.append(float(value))
        somma = somma + value
print ('{}\n'.format(values)) #stampo tutti i miei valori
#provo a definire una funzione somma
def sum_list(the_list):
    somma = 0
    for item in the_list:
        somma = somma + item
    return somma
controllo = sum_list(values)
#if di controllo per vedere se le due funzioni calcolano nella stessa maniera
if controllo == somma:
    print ('Il programma funziona! Il risultato calcolato è: {}' .format(somma))
elif controllo != somma:
    print ('Qualcosa non sta funzionando... La prima funzione ha calcolato {}, la seconda invece {}' .format(somma) .format(controllo))
my_file.close()
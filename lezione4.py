class CSVfile ():
    def __init__ (self, name):
        self.name = name
    def __str__ (self):
        return 'Nome file: {}' .format(self.name)
    def get_data (self):
        values = []
        data = []
        my_file = open (self.name)
        for line in my_file:
#divido gli elementi in base a dov'è la virgola
            elements = line.split(',')
#se la riga non è Date, allora mi salvo il valore in value
            if elements[0] != 'Date':
                value = elements[1]
                values.append(value)
                data = elements[0]
                values.append(data)
                print ("[{}] [{}]" .format (data, value[0: -1]))
            elif elements[0] == 'Date':
                print ("{}" .format(elements))
        my_file.close
fily = CSVfile("shampoo_sales.csv")
print (fily)
print (fily.name)
fily.get_data()
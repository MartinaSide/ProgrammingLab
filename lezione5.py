class CSVfile ():
    def __init__ (self, name):
        self.name = name
    def __str__ (self):
        return 'Nome file: {}' .format(self.name)
    def get_data (self):
        values = []
        data = []
        try:
            my_file = open (self.name)
        except FileNotFoundError:
            print ("Ho avuto un errore: IL FILE NON ESISTE. Il nome del file era: {}" .format(self.name))
            self.name = ("shampoo_sales.csv")
        except Exception as e:
            print ("Errore generico")
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
    def NumericalCSVFile (self):
        values = []
        data = []
        try:
            my_file = open (self.name)
        except FileNotFoundError:
            print ("Ho avuto un errore: IL FILE NON ESISTE. Il nome del file era: {}" .format(self.name))
            self.name = ("shampoo_sales.csv")
        except Exception as e:
            print ("Errore generico")
        my_file = open (self.name)
        for line in my_file:
#divido gli elementi in base a dov'è la virgola
            elements = line.split(',')
#se la riga non è Date, allora mi salvo il valore in value
            if elements[0] != 'Date':
                try:
                    value = float (elements[1] [0:-1])
                except ValueError:
                    (elements[1] [0:-1])
                    print ("Ho avuto un errore di tipo VALUE :(")
                    print ("Il valore che mi ha dato problemi è stato: {}" .format(elements))
                except TypeError:
                    value = (elements[1] [0:-1])
                    print ("Ho avuto un errore di tipo TYPE")
                    print ("Il valore che mi ha dato problemi è stato: {}" .format(elements))
                except Exception as e:
                    print ("Ho avuto un errore generale... non posso dirti di più, mi dispiace :(")
                    print ("Il valore che mi ha dato problemi è stato: {}" .format(elements))
                values.append(value)
                data = elements[0]
                values.append(data)
                print ("[{}] [{}]" .format (data, value))
            elif elements[0] == 'Date':
                print ("{}" .format(elements))
        my_file.close
fily = CSVfile("shampoo_sales.csv")
print (fily)
print (fily.name)
fily.NumericalCSVFile()
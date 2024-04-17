import matplotlib.pyplot as plt

def plot_column(DataBase,column_G):
    column_data = tuple(row[column_G] for row in DataBase)
    converted_column = []

    for value in column_data[1:]:
        converted_column.append(value)
        
    plt.plot(converted_column)
    plt.xlabel('# De datos')
    plt.ylabel('Corriente 1')
    plt.title('Gráfico de Corriente de linea 1')
    plt.grid(True)
    plt.show()

def plot_column1(DataBase,column_G1):
    column_data1 = tuple(row[column_G1] for row in DataBase)
    converted_column1 = []

    for value in column_data1[1:]:
        converted_column1.append(value)
        
    plt.plot(converted_column1)
    plt.xlabel('# De datos')
    plt.ylabel('Corriente 2')
    plt.title('Gráfico de Corriente de linea 2')
    plt.grid(True)
    plt.show()

def plot_column2(DataBase,column_G2):
    column_data2 = tuple(row[column_G2] for row in DataBase)
    converted_column2 = []

    for value in column_data2[1:]:
        converted_column2.append(value)
        
    plt.plot(converted_column2)
    plt.xlabel('# De datos')
    plt.ylabel('Corriente 3')
    plt.title('Gráfico de Corriente de linea 3')
    plt.grid(True)
    plt.show()
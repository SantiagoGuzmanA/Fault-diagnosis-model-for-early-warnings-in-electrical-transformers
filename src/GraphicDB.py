import matplotlib.pyplot as plt

def plot_column(DataBase,column_G):
    column_data = tuple(row[column_G] for row in DataBase)
    converted_column = []

    for value in column_data[1:]:
        converted_column.append(value)
        
    plt.plot(converted_column)
    plt.xlabel('# De datos')
    plt.ylabel('Voltaje')
    plt.title('Gráfico de Voltaje')
    plt.grid(True)
    plt.show()
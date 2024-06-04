import matplotlib.pyplot as plt
from PowerCalculation import*
def plot_column(DataBase,column_G):
    column_data = [row[column_G] for row in DataBase[1:]]

    plt.figure(figsize=(12, 6))
    plt.plot(column_data)
    plt.xlabel('# Of data')
    plt.ylabel('Current 1')
    plt.title('Line 1 Current Graph')
    plt.grid(True)
    plt.show()

def plot_column1(DataBase,column_G1):
    column_data1 = [row[column_G1] for row in DataBase[1:]]

    plt.figure(figsize=(12, 6))
    plt.plot(column_data1)
    plt.xlabel('# Of data')
    plt.ylabel('Current 2')
    plt.title('Line 2 Current Graph')
    plt.grid(True)
    plt.show()

def plot_column2(DataBase, column_G2):
    column_data2 = [row[column_G2] for row in DataBase[1:]]

    plt.figure(figsize=(12, 6))
    plt.plot(column_data2)
    plt.xlabel('# Of data')
    plt.ylabel('Current 3')
    plt.title('Line 3 Current Graph')
    plt.grid(True)
    plt.show()

def plot_power(DataBase):
    powers = calculate_power_per_recordOP(DataBase)

    plt.figure(figsize=(12, 6))

    plt.plot(powers, color='r')

    plt.xlabel('# Of data')
    plt.ylabel('Power (KvA)')
    plt.title('Power graph per record')

    plt.grid(True)

    plt.show()

def plot_power_bar(DataBase):
    powers = calculate_power_per_recordOP(DataBase)
    indices = range(1, len(powers) + 1)

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(indices, powers, color='red', alpha=0.7)

    ax.set_xlabel('# Of data')
    ax.set_ylabel('Power (KvA)')
    ax.set_title('Power graph per record (Bars)')

    plt.show()
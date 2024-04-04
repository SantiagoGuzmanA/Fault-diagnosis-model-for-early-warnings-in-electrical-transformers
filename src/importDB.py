def importDB(DataBase):
    try:
        fhand = open(DataBase)
    except:
        print("El archivo .txt no existe en la ruta especificada")
        quit()
    
    DB = []
    for line in fhand:
        row = [float(value) if value.replace('.', '', 1).isdigit() else value for value in line.strip().split(',')]
        DB.append(row)
    return(DB)

fname = input("Ingrese el nombre del archivo: ")
DB = importDB(fname)
for i in DB:
    print(i) 
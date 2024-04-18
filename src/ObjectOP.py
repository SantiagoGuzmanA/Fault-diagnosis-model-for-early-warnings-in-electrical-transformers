class DataBaseHandling:
    def __init__(self,path:str,I1=4,I2=5,I3=6):
        self.path = path
        self.I_Columns = [I1,I2,I3]
        self.__DB__ = self.__importDB__(self.path)
        self.__DBZ__ = self.__deleteZeros__(self.__DB__,self.I_Columns)
        self.Power = []
        self.SD_I1: float = None
        self.SD_I2: float = None
        self.SD_I3: float = None
        self.Upper_Limit_I1: float = None
        self.Lower_Limit_I1: float = None
        self.Upper_Limit_I2: float = None
        self.Lower_Limit_I2: float = None
        self.Upper_Limit_I3: float = None
        self.Lower_Limit_I3: float = None
    
    def __importDB__(self,path:str):
        try:
            fhand = open(path)
        except:
            print("El archivo .txt no existe en la ruta especificada")
            quit()
        
        DB = []
        for line in fhand:
            row = [float(value) if value.replace('.', '', 1).isdigit() else value for value in line.strip().split(',')]
            DB.append(row)
        return(DB)
    
    def __deleteZeros__(self,DB:list,Columns:list):
        try:
            if not isinstance(DB,list):
                raise TypeError("La entrada de la funcion para eliminar los ceros de la columna de voltage no es un arreglo")
        except TypeError as Error:
            print(Error)
        
        DBZ=[]
        for row in DB:
            if all(row[Column] == 0 for Column in Columns):
                continue
            else:
                DBZ.append(row)
        return(DBZ)
    
    def getDB (self):
        return self.__DB__
    
    def getDBZ (self):
        return self.__DBZ__

Base_de_Datos = DataBaseHandling("DatosMonitoringTransformer.txt")
print(len(Base_de_Datos.getDB()))
print(len(Base_de_Datos.getDBZ()))
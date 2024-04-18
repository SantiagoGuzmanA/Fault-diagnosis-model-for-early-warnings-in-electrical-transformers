class DataBaseHandling:
    def __init__(self,path:str,I1=4,I2=5,I3=6):
        self.path = path
        self.I1_Column = I1
        self.I2_Column = I2
        self.I3_Column = I3
        self.DB = []
        self.DBZ = []
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
    
    def __importDB__(self,path):
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
import math, time
class DataBaseCheck:
  def __init__(self,DB:list):
    self.__DB__ = DB
    self.__boolean__ = self.__check__()

  def __check__(self):
    if isinstance(self.__DB__,list):
      return True
    else:
      return False

class DelZeros(DataBaseCheck):
  def __init__(self,DB:list,Columns:list):
    super().__init__(DB)
    self.__Columns__ = Columns
    st = time.time()
    self.__DBZ__ = self.__deleteZeros__()
    et = time.time()
    print(f'Elapsed execution time for DeleteZeros: {(et-st)*1000} ms\n')

  def __deleteZeros__(self):
    try:
      if not self.__boolean__:
        raise TypeError("The database must be List type")
    except TypeError as Error:
      print(Error)

    Temp_DBZ = [row for row in self.__DB__ if not all(row[column] == 0 for column in self.__Columns__)]
    return(Temp_DBZ)

  def getDBZ(self):
    return self.__DBZ__

class PowerCalculation(DataBaseCheck):
  def __init__(self,DB:list):
    super().__init__(DB)
    st = time.time()
    self.__Powers__ = self.__calculate_power_per_record__()
    et = time.time()
    print(f'Elapsed execution time for PowerCalculation: {(et-st)*1000} ms\n')
  def __calculate_power_per_record__(self):
    try:
      if not self.__boolean__:
        raise TypeError("The database must be List type")
    except TypeError as Error:
      print(Error)
    Powers=[]
    for register in self.__DB__[1:]:
        phase_voltages = register[1:4]
        currents = register[4:7]

        sum_phase_voltages = sum(phase_voltages)
        len_phase_voltages = len(phase_voltages)
        sum_currents = sum(currents)
        len_currents = len(currents)

        vf_average = sum_phase_voltages / len_phase_voltages
        vl = math.sqrt(3) * vf_average
        I_average = sum_currents / len_currents

        power_registration = (math.sqrt(3) * vl * I_average) / 1000
        approximate_power = round(power_registration, 2)
        Powers.append(approximate_power)

    return Powers

  def getPowers(self):
    return self.__Powers__

class StandardDeviaton(DataBaseCheck):
    def __init__(self,DB):
        super().__init__(DB)
        self.__n__ = len(self.__DB__[1:])
        st = time.time()
        self.__avg__ = self.__average__()
        self.__SD__ = self.__standadDeviaton__()
        self.__Limits__ = self.__limits__()
        et = time.time()
        print(f'Elapsed execution time for StandardDeviaton : {(et-st)*1000} ms\n')
    def __average__(self):
        try:
            if not self.__boolean__:
                raise TypeError("The database must be List type")
        except TypeError as Error:
            print(Error)

        if self.__n__ <= 1:
            return []
        I1_sum = 0
        I2_sum = 0
        I3_sum = 0

        for row in self.__DB__[1:]:
            I1_sum += row[4]
            I2_sum += row[5]
            I3_sum += row[6]

        return [I1_sum / self.__n__, I2_sum / self.__n__, I3_sum / self.__n__]

    def __standadDeviaton__(self):
        try:
            if not self.__boolean__:
                raise TypeError("The database must be List type")
        except TypeError as Error:
            print(Error)

        DistMediaI1_sum = 0
        DistMediaI2_sum = 0
        DistMediaI3_sum = 0

        for row in self.__DB__[1:]:
            DistMediaI1_sum +=(row[4] - self.__avg__[0]) ** 2
            DistMediaI2_sum +=(row[5] - self.__avg__[1]) ** 2
            DistMediaI3_sum +=(row[6] - self.__avg__[2]) ** 2

        return [round(math.sqrt(DistMediaI1_sum / self.__n__),2), round(math.sqrt(DistMediaI2_sum / self.__n__),2), round(math.sqrt(DistMediaI3_sum / self.__n__),2)]

    def __limits__(self):
        return [[self.__avg__[0] + self.__SD__[0], self.__avg__[0] - self.__SD__[0]],[self.__avg__[1] + self.__SD__[1], self.__avg__[1] - self.__SD__[1]],[self.__avg__[2] + self.__SD__[2],self.__avg__[2] - self.__SD__[2]]]

    def getSD(self):
        return self.__SD__

    def getavg(self):
        return self.__avg__

    def getLimits(self):
        return self.__Limits__

class DataBaseHandling:
    def __init__(self,path:str,I1=4,I2=5,I3=6):
        self.__Path__ = path
        self.__I_Columns__ = [I1,I2,I3]
        self.__DB__ = self.__importDB__(self.__Path__)
        self.__DBZ__ = DelZeros(self.__DB__,self.__I_Columns__)
        self.__PW__ = PowerCalculation(self.__DBZ__.getDBZ())
        self.Power = []
        self.__SD__ = StandardDeviaton(self.__DBZ__.getDBZ())

    def __importDB__(self,path:str):
        try:
            fhand = open(path)
        except:
            print("The .txt file does not exist in the specified path")
            quit()

        DB = []
        for line in fhand:
            row = [float(value) if value.replace('.', '', 1).isdigit() else value for value in line.strip().split(',')]
            DB.append(row)
        return(DB)

    def getDB (self):
        return self.__DB__

    def getDBZ (self):
        return self.__DBZ__.getDBZ()

    def getPowers (self):
        return self.__PW__.getPowers()

    def getSD (self,index:int=0):
      if index == 0:
        return self.__SD__.getSD()
      elif index == 1:
        return self.__SD__.getLimits()
      elif index == 2:
        return self.__SD__.getavg()

Base_de_Datos = DataBaseHandling("DatosMonitoringTransformer.txt")
print("Script for the Database call")
print(f"Have been loaded {len(Base_de_Datos.getDB())} records.\n")
print("Script for the DeleteZeros")
print(f"Database size without zeros:  {len(Base_de_Datos.getDBZ())}\n")
print("Script for the PowerCalculation")
print("Primeros 30 valores de potencias:")
for i, (register, power) in enumerate(zip(Base_de_Datos.getDBZ()[1:30], Base_de_Datos.getPowers()[:30]), start=1):
    print(f"Register {i}: Data = {register}, Power = {power} KvA")
print("\n")
DE1, DE2, DE3 = Base_de_Datos.getSD()
print(f"Standard deviation I1: {DE1}")
print(f"Standard deviation I2: {DE2}")
print(f"Standard deviation I3: {DE3}\n")

limits = Base_de_Datos.getSD(1)
print(f"Upper limit I1: {limits[0][0]}")
print(f"Lower limit I1: {limits[0][1]}")
print(f"Upper limit I2: {limits[1][0]}")
print(f"Lower limit I2: {limits[1][1]}")
print(f"Upper limit I3: {limits[2][0]}")
print(f"Lower limit I3: {limits[2][1]}\n")
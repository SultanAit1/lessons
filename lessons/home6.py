
class Hero:

    def __init__(self, power=0, fly=0, skill=0, magic=0):

        self.__power = power
        self.__fly = fly
        self.__skill = skill
        self.__magic = magic
    def setpwr(self, power):
        self.__power = power
    def getpwr(self):
        return self.__power
    def setfly(self, fly):
        self.__fly = fly
    def getfly(self):
        return self.__fly
    def setskill(self, skill):
        self.__skill = skill
    def getskill(self):
        return self.__skill
    def setmgc(self, magic):
        self.__magic = magic
    def getmgc(self):
        return self.__magic
hr = Hero()
hr.setpwr(33)
hr.setfly(1)
hr.setskill(100)
hr.setmgc(24)
print(f'pw-{hr.getpwr()} \n'
f'fly-{hr.getfly()} \n'
f'skill-{hr.getskill()} \n'
f'Магия-{hr.getmgc()}')

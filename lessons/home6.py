
class Hero:

    def __init__(self, power=True, fly=True, skill=True, csco=True):

        self.__power = power
        self.__fly = fly
        self.__skill = skill
        self.__csco = csco
    def setpower(self, power):
        self.__power = power
    def getpower(self):
        return self.__power
    def setfly(self, fly):
        self.__fly = fly
    def getfly(self):
        return self.__fly
    def setskill(self, skill):
        self.__skill = skill
    def getskill(self):
        return self.__skill
    def setcsco(self, csco):
        self.__csco = csco
    def getcsco(self):
        return self.__csco
hr = Hero()
hr.setpower(101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010)
hr.setfly(1)
hr.setskill('cut')
hr.setcsco('Ak-47')
print(f'pw-{hr.getpower()} \n'
f'fly-{hr.getfly()} \n'
f'skill-{hr.getskill()} \n'
f'Магия-{hr.getcsco()}')

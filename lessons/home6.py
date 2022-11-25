class Hero:
    head = 1

    def __init__(self,name,skill,hp):
        self.name=name
        self.skill = skill
        self.hp = hp

    @property
    def hello(self):
        print('my name is ' + self.name)

    @property
    def fly(self):
        print(f'{self.name} is flying')

    @property
    def heal(self,plus):
        print(self.hp + plus)

    @property
    def phrase(self):
        print('i won')


    @hello.setter
    def hello(self,new_hello):
        self.new_hello = new_hello

    @fly.setter
    def fly(self,new_fly):
        self.new_fly = new_fly


    @heal.setter
    def heal(self,new_heal):
        self.new_heal = new_heal

    @phrase.setter
    def phrase(self,new_phrase):
        self.new_phrase = new_phrase
    


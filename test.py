class Coffee:
  pass

class Child:
    characteristic = "Hooman"
    def __init__(self,name,age):
        self.name = name
        self.age = age

class Account:
    def __init__(self):
        self.username = None
        self.__pwd = None

    def set_id(self,username):
        self.username = username

    def set_pwd(self,pwd):
        self.__pwd = pwd

class Animal:
    def __init__(self,name):
        self.name = name

    def getName(self):
        return self.name

class Cheetah(Animal):
    def __init__(self,name,diet):
        Animal.__init__(self,name)
        self.diet = diet

    def getDiet(self):
        return self.getName() + "'s diet is: " + self.diet

class Pigeon(Animal):
    def __init__(self,name,sound):
        super().__init__(name)
        self.sound = sound

    def getSound(self):
        return self.sound

class Fish(Animal):
    def __init__(self,name,movement):
        super(Fish,self).__init__(name)
        self.movement = movement

    def getMovement(self):
        return self.movement

    def getName(self):
        return self.name + "is a fish"



ani = Animal("myAnimal")
c = Cheetah("Petite Kitty","Carnivore")
p = Pigeon("Birdie","Roekoeee")
f = Fish("Nemo","Just keeps swimming")


ani.getName()
c.getName()
c.getDiet()
p.getSound()
p.getName()
f.getName()
f.getMovement()
if __name__ == "__main__":
  acc = Account()
  print(acc.username)
  acc.username = "Lulu"
  print(acc.username)
  acc.set_pwd("uncrackable")
  acc.__dict__
  print(acc.pwd)

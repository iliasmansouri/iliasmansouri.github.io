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
        return self.name + " is a fish"

class mySingleton(object):
    def __new__(singleClass):
        if not hasattr(singleClass, 'instance'):
            singleClass.instance = super(mySingleton,singleClass).__new__(singleClass)
        return singleClass.instance

class lazySingleton(object):
    __instance = None
    def __init__(self):
        if not lazySingleton.__instance:
            print("Calling init method")
        else:
            print("Instance already present")
    @classmethod
    def getInstance(singleClass):
        if not singleClass.__instance:
            singleClass.__instance = lazySingleton()
        return singleClass.__instance

class Borg:
    __borg_state = {"x":"1"}
    def __init__(self):
        self.__dict__ = self.__borg_state
        pass

b = Borg()
print(b.__dict__)

b2 = Borg()
print(b2.__dict__)
b.y = 3
print(b.__dict__)


from abc import ABCMeta, abstractmethod

class Dog(metaclass = ABCMeta):
    @abstractmethod
    def race_name(self):
        pass

class Dachshund(Dog):
    def race_name(self):
        print("Dachshund")

class Labrador(Dog):
    def race_name(self):
        print("Labrador")

doggo = Dachshund()
doggo.race_name()

labbie = Labrador()
labbie.race_name()



from abc import ABCMeta, abstractmethod

class Part(metaclass=ABCMeta):
    @abstractmethod
    def description(self):
        pass

class Head(Part):
    def description(self):
        print("This is the cyborg's head")

class Torso(Part):
    def description(self):
        print("This is the cyborg's torso")

class Legs(Part):
    def description(self):
        print("This is the cyborg's legs")

class Arms(Part):
    def description(self):
        print("This is the cyborg's arms")

class Wheels(Part):
    def description(self):
        print("This is the cyborg's wheels")

class Thruster(Part):
    def description(self):
        print("This is the cyborg's thruster")

class Borg(metaclass=ABCMeta):
    def __init__(self):
        self.parts = []
        self.createBorg()
    @abstractmethod
    def createBorg(self):
        pass
    def getParts(self):
        return self.parts
    def addPart(self,part):
        self.parts.append(part)

class defaultBorg(Borg):
    def createBorg(self):
        self.addPart(Head())
        self.addPart(Torso())
        self.addPart(Legs())
        self.addPart(Arms())

class airBorg(Borg):
    def createBorg(self):
        self.addPart(Head())
        self.addPart(Torso())
        self.addPart(Thruster())

humanoid = defaultBorg()
humanoid.getParts()

flyer = airBorg()
flyer.getParts()


s = lazySingleton()
s

s.getInstance()
s2 = lazySingleton()
s3 = lazySingleton()

s = mySingleton()
print(s)
s2 = mySingleton()
print(s2)

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
f.getName()

if __name__ == "__main__":
  acc = Account()
  print(acc.username)
  acc.username = "Lulu"
  print(acc.username)
  acc.set_pwd("uncrackable")
  acc.__dict__
  print(acc.pwd)

---
title: "Design Patterns with Python Part 2: The Factory"
date: 2018-05-23
tags: [Design Patterns]
excerpt: "Python, Design Patterns, OOP"
---
# Enter the Factory
A factory creates objects. Yes I know, mindblowing stuff. Furthermore, we can comfortably say that a factory creates different type of objects but in the greater scheme of life those objects are similar in nature. Succinctly, a factory create objects of another type. Meaning, factory cannot create a factory.

## Simple Factory Pattern
The simplest form of the Factory DP, is to have a methodology to create different types of objects. As we see below, no direct object instantiation happens.

{% highlight python %}
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
{% endhighlight %}

ABCMeta is a Python metaclass which can be used to design a class as abstract. Our abstract class, Dog that is, has the *race_name()* method. Once the metaclass defined, we can reuse this through inheritance. The abstractmethod decorator is needed because a class that has a metaclass derived from ABCMeta cannot be instantiated unless all abstract methods/properties are overriden.

## Factory Method Pattern
The Factory Method pattern expands on the previous one and will basically take care of following enhancements:
* An interface is created for object creation. From this, the subclass is responsible for object creation and not the factory
This will result in a much more flexible and customizable design. Furthermore, the loos coupling results in an easy high level interface, easily maintainable where the user/client doesn't have to bother with arguments and instantiations.

Firstly, we define the so-called "Product Interface". This is done by defining the different parts from which a cyborg can be created. Afterwards, we define the "Creator". In our case, this is the class Borg which provides a factory method *createBorg()*. The Creator class doesn't know about the needed parts for creating a Borg. That's where the defaultBorg- and airBorg class comes in play, aka the "ConcreteCreator classes". Both classes, implement the createBorg() abstract method and their respective parts methods at runtime.

{% highlight python %}
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
{% endhighlight %}

## Abstract Factory pattern
This takes the factory pattern and further by applying a mechanic in which an interface is created in which different related objects can be created without specifying the concrete classes.

Firstly, the abstract base class PizzaFactory is defined with its two abstract methods. The 2 concrete factories are IndianPizzaFactory and USPizzaFactory. No surprises here.

Secondly, we define the abstractions for our products, which are VegPizza and NonVegPizza with each their methods. So identical products from different factories can be differently made.

Those different concrete products: DeluxVeggiePizza, ChickenPizza, HamPizza, MexicanVegPizza are then each defined with appropriate methods.


{% highlight python %}
from abc import ABCMeta, abstractmethod

class PizzaFactory(metaclass=ABCMeta):
  @abstractmethod
  def createVegPizza(self):
    pass

  @abstractmethod
  def createNonVegPizza(self):
    pass

class IndianPizzaFactory(PizzaFactory):
  def createVegPizza(self):
    return DeluxVeggiePizza()
  def createNonVegPizza(self):
    return ChickenPizza()

class USPizzaFactory(PizzaFactory):
  def createVegPizza(self):
    return MexicanVegPizza()
  def createNonVegPizza(self):
    return HamPizza()

class VegPizza(metaclass=ABCMeta):
  @abstractmethod
  def prepare(self, VegPizza):
    pass

class NonVegPizza(metaclass=ABCMeta):
  @abstractmethod
  def serve(self, VegPizza):
    pass

class DeluxVeggiePizza(VegPizza):
  def prepare(self):
    print("Prepare ", type(self).__name__)

class ChickenPizza(NonVegPizza):
  def serve(self, VegPizza):
    print(type(self).__name__, " is served with Chicken on ",
    type(VegPizza).__name__)

class MexicanVegPizza(VegPizza):
  def prepare(self):
    print("Prepare ", type(self).__name__)

class HamPizza(NonVegPizza):
  def serve(self, VegPizza):
    print(type(self).__name__, " is served with Ham on ",
    type(VegPizza).__name__)

indianfactory = IndianPizzaFactory()
vp = indianfactory.createVegPizza()
non_vp = indianfactory.createNonVegPizza()
vp.prepare()
non_vp.serve(vp)

usfactory = USPizzaFactory()
vp = usfactory.createVegPizza()
non_vp = usfactory.createNonVegPizza()
vp.prepare()
non_vp.serve(vp)
{% endhighlight %}


Et voila! Now go fetch dat pizza and pat yeself hooman.

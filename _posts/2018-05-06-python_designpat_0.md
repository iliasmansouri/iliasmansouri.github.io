---
title: "Design Patterns with Python: Part 0"
date: 2018-05-06
tags: [Design Patterns]
excerpt: "Python, Design Patterns, OOP"
---

# Object Oriented Programming (OOP)
Just to have an introduction and conform to the laws of blogging, a definition unashamedly copy-pasta'd from holy wiki:

*Object-oriented programming (OOP) is a programming paradigm based on the concept of "objects", which may contain data, in the form of fields, often known as attributes; and code, in the form of procedures, often known as methods.*

Now let's get practical, shall we?

# Classes in Python
First of all: everything is a class in Python. Yup, that's right. Everything. Functions, methods, lists or floats. So, how easy is it to further enlarge the classy realm?

{% highlight python %}
class Coffee:
  pass

if __name__ == "__main__":
  cup = Coffee()
{% endhighlight %}


Easy, yah? You could even create a reference to cup like this:

{% highlight python %}
class Coffee:
  pass

if __name__ == "__main__":
  cup = Coffee()
  c = cup
{% endhighlight %}


No need for seeing stars C-style. The pass statement is just an easy way to create an empty class without Python raining them errors over you.

## Attributes
Attributes simply are *properties* of a Class. Hence, attributes are creates within the scope of a class definition. Even though, attributes and properties are synonyms in the English language or even in different context, we will later see that properties have their own meaning within Python.

You could create attributes as following:

{% highlight python %}
class Coffee:
  pass

if __name__ == "__main__":
  cup = Coffee()
  cup.brew = "Ethopian"
{% endhighlight %}


This is not considered as good practice and thus should be avoided.

### Instance Attributes
As mentioned earlier, attributes are defined within it's respective class. If you are just learning the basics in python I strongly recommend to not learn the quick-and-dirty approach. Starting from next blog, we will start delving into Design Patterns which will force you to be a smexy programmer. Resisting will only cause in loss of hair, life and perhaps even teeth. And just admits its... You'd like to be smexy, don't you?

{% highlight python %}
class Child:
    def __init__(self,name,age):
        self.name = name
        self.age = age

if __name__ == "__main__":
  c = Child("Ilias",44)
  c.__dict__
{% endhighlight %}


A bit more happening in here. The __init__ method is a way to define attributes right after creation of an instance. Moreover, the __init__() method is called automatically when you create an instance and thus you will never have to call this method.

Internally Python will replace the 'self' with the correct instance. The *self* variable is needed to id every unique instance of a class. If you simply *Class.attribute = val* and you have multiple instances of this Class, there would be no way for Python to know which instance of the Class you want to instantiate.

The __dict__ is a neat trick to inspect an instance's attribute.

### Class Attributes
Instance attributes are unique for each instance of a class while Class Attributes are parameters which are identical to all instances of a class. Below, we can see that every Child created has the Hooman characteristic but has their name and age attributes.

{% highlight python %}
class Child:
    characteristic = "Hooman"

    def __init__(self,name,age):
        self.name = name
        self.age = age

if __name__ == "__main__":
  c = Child("Ilias",44)
  c.__dict__
{% endhighlight %}

# Abstraction
Data Abstraction is a broad term which is the culmination of 2 principles. On the one hand, Encapsulation which basically consist in encapsulating parameters and their respective methods. While on the other hand, Data Hiding occurs to prevent that parameters can't be changed if required.
## Encapsulation
Encapsulation in the O.O.P. world is synonym with getters and setters methods.

{% highlight python %}
class Account:
    def __init__(self):
        self.username = None
        self.pwd = None

    def set_id(self,username):
        self.username = username

    def set_pwd(self,pwd):
        self.pwd = pwd

if __name__ == "__main__":
  acc = Account()
  print(acc.username)
  acc.username = "Lulu"
  print(acc.username)
{% endhighlight %}

Above an example of using setters and getters method. As you can see, it's still possible to change the parameters with the *.* accessor. Primarily, this can cause security issues. Secondly, this results that their are at least 2 ways of instantation which is highly unpythonic.

This is solved by using private attributes which brings us nicely to the next topic.

## Hiding
By using the prefix *__* in front of an attribute, we declare that this attribute is private. Concretely, this private attribute can only be used inside the Class itself. Indeed, the attribute is invisible and inaccessible from the external realm and can only be accessed/modified by methods which resides in the class themselves.

{% highlight python %}
class Account:
    def __init__(self):
        self.username = None
        self.__pwd = None

    def set_id(self,username):
        self.username = username

    def set_pwd(self,pwd):
        self.__pwd = pwd

if __name__ == "__main__":
  acc = Account()
  print(acc.username)
  acc.username = "Lulu"
  print(acc.username)
  acc.set_pwd("uncrackable")
  acc.__dict__
  print(acc.pwd)
{% endhighlight %}

Interestingly, the last print-statement in the code above may result in your loss of faith in this world and I thus highly encourage you to try it out.

There is also the *_* prefix which declares a protected attribute. This is used to tell programmers to touch this aatribute only if a subclass is created. This will become clear later on but first we need to explain the concept of Inheritance...

# Inheritance
Inheritance can be easily explained as an *is-a* relationship: 'An employee is a human','A spider is an insect', 'Pizza is a food', etc. Below, you find a basic example of the Inheritance concept:

{% highlight python %}
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
{% endhighlight %}

As you see, a sub class gets its base class as input. Afterwards, we observe 3 ways to initialize the Animal superclass. In the Fish class we also see how to override a method. This is useful as you can define a superclass with default methods as behaviour and depending on the subclasses can modify/override specific behaviours. As we will in the next blog, this is a powerful tool in Design Patterns concepts.

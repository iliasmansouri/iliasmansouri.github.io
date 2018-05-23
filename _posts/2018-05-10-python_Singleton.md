---
title: "Design Patterns with Python Part 1: The Singleton"
date: 2018-05-09
tags: [Design Patterns]
excerpt: "Python, Design Patterns, OOP"
---

# What is a Design Pattern?
**Wiki:** *reusable solution to a commonly occurring problem within a given context*. Moreover, Design Patterns have withstood the trials of time and mostly keep scalability and efficiency in mind.

As you can see below, Design Patterns are typically divided in 3 groups and for each group you find the respective patterns:

* Creational Patterns
  * Singleton
  * Abstract Factory
  * Factory Method
  * Builder
  * Prototype
* Behavioral Patterns
  * Visitor
  * Template
  * State
  * Strategy
  * Observer
  * Memento
  * Mediator
  * Interpreter
  * Iterator
  * Command
  * Chain of Responsibility
* Structural Patterns
  * Facade
  * Decorator
  * Flyweight
  * Proxy
  * Bridge  
  * Composite
  * Adapter

As the name suggest, Creational Design Patterns takes care of the creation of objects. Structural DP's let's you reuse classes to build larger class structures. Finally, Behavioral DP's are more about the interfacing and communication of objects.

Let's get started with our first Design Pattern, as this is the main reason why we're all here!

The Singleton is a practice to create a single object which then can be used/shared with other objects. Only one object of this class exist and therefore a mechanism should be set to avoid further object creation.

Where are those used? In logging-, Service- and Caching services. Also for loggers, load balancer, window management in OS, interface to a database, etc.

{% highlight python %}
class mySingleton(object):
    def __new__(singleClass):
        if not hasattr(singleClass, 'instance'):
            singleClass.instance = super(mySingleton,singleClass).__new__(singleClass)
        return singleClass.instance

s = mySingleton()
print(s) #<__main__.mySingleton object at 0x7f6524add198>
s2 = mySingleton()
print(s2) #<__main__.mySingleton object at 0x7f6524add198>
{% endhighlight %}

With the *__new__* prefix we override Python's default method to instantiate an object. First we check if the object doesn't exist with *hasattr*. Basically, it checks if *singleClass* has already an object. If not, we create this instance and returns it. If multiple instance are run with the creation of the object, the existing mySingleton will be returned.

Below, we observe identical behaviour only that when *Singleton()* is called no actual instance is created. The creation only happens when the *getInstance()* function is called. This results in a more efficient ressource allocation as the object is only created when needed.

{% highlight python %}
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

s = lazySingleton()

s.getInstance()        
s2 = lazySingleton()
s3 = lazySingleton()
{% endhighlight %}

Above, we saw how the Singleton Pattern is used when one unique instance is created and managed. Another way is that different Singletons share their state. The clue is to assign the *__dict__* variable to the class variable you want it to be shared with all other classes.

{% highlight python %}
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
{% endhighlight %}

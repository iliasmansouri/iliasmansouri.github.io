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
{% highlight python %}

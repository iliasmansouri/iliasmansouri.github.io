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

'''python
    class Coffee:
      pass

    if __name__ == "__main__":
      cup = Coffee()
'''

Easy, yah? You could even create a reference to cup like this:

'''python
    class Coffee:
      pass

    if __name__ == "__main__":
      cup = Coffee()
      c = cup
'''

No need for seeing stars C-style. The pass statement is just an easy way to create an empty class without Python raining them errors over you.

## Attributes
Attributes simply are *properties* of a Class. Hence, attributes are creates within the scope of a class definition. Even though, attributes and properties are synonyms in the English language or even in different context, we will later see that properties have their own meaning within Python.

You could create attributes as following:

'''python
    class Coffee:
      pass

    if __name__ == "__main__":
      cup = Coffee()
      cup.brew = "Ethopian"
'''

This is not considered as good practice and thus should be avoided.

### Instance Attributes
As mentioned earlier, attributes are defined within it's respective class. If you are just learning the basics in python I strongly recommend to not learn the quick-and-dirty approach. Starting from next blog, we will start delving into Design Patterns which will force you to be a smexy programmer. Resisting will only cause in loss of hair, life and perhaps even teeth. And just admits its... You'd like to be smexy, don't you?

'''python
    class Child:
        def __init__(self,name,age):
            self.name = name
            self.age = age

    if __name__ == "__main__":
      c = Child("Ilias",44)
      c.__dict__
'''

A bit more happening in here. The __init__ method is a way to define attributes right after creation of an instance. Moreover, the __init__() method is called automatically when you create an instance and thus you will never have to call this method .

Internally Python will replace the 'self' with the correct instance. The 'self' variable is needed to id every unique instance of a class. If you simply 'Class.attribute = val' and you have multiple instances of this Class, there would be no way for Python to know which instance of the Class you want to instantiate.

The '__dict__' is a neat trick to inspect an instance's attribute.

### Class Attributes

# Instance & Instantiation

# Inheritance

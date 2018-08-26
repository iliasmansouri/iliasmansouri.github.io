---
title: "Design Patterns with Python Part 3: The Façade"
date: 2018-06-01
tags: [Design Patterns]
excerpt: "Python, Design Patterns, OOP"
---

# La jolie Façade
A façade usually means the front of a building or a deceptive external appearance. In what way is the Façade pattern using its deception? By providing a simple interface to the user which veils the complexities of underlying system.

Let's dive into it as an example will clarify the concept! Our Façade will be a new revolutionary Operating System. Indeed, our OS will provide an enhanced UI experience with its sleek, elegant and simple interface. As you all now, the underlying system/complexity consists of the different hardware components and their interactions. Therefore, we will create a Façade in which OS related tasks appear deceptively simple to the end-user.

{% highlight python %}
class myOS(object):
    def __init__(self):
        print("\n---------------Welcome to myOS!---------------\n")

    def bootup(self):
        self.inout = InOut()
        self.inout.check()

        self.disks = Disks()
        self.disks.detect()

        self.ui = UI()
        self.ui.start()

        self.preferences = Prefs()
        self.preferences.load()

        print("\n---------------myOS ready for enjoyment!---------------\n")

class InOut(object):
    def __init__(self):
        print('---Checking for Input and Outpus devices...')
    def __hardwareOK(self):
        print('---Hardware checks running')
        return True
    def check(self):
        if self.__hardwareOK():
            print("IO devices all healthy and up to date! \n")


class Disks(object):
    def __init__(self):
        print("---Detecting SSD's and HDD's...")

    def runMemDetection(self):
        pass

    def detect(self):
        self.runMemDetection()
        print('Detected 1 HDD of 1TB and SSD with 256GB.\n')

class UI(object):
    def __init__(self):
        print('---Running the UI service...')

    def detectBestRes(self):
        pass

    def detectHardwareAcc(self):
        pass
    def start(self):
        self.detectBestRes()
        self.detectHardwareAcc()
        print('UI up and running optimized for your system specs!\n')

class Prefs(object):
    def __init__(self):
        print("---Applying your preferences")
    def load(self):
        print("Your preferences have been taken into account!\n")

class endUser(object):
    def __init__(self):
        print("Let's geek on dis beastie")

    def pushPowerButton(self):
        print("I love the sensation of pressing dats power button...")
        myInstance = myOS()
        myInstance.bootup()

user = endUser()
user.pushPowerButton()

{% endhighlight %}

The class myOS functions here as a Façade. As we can see, when an endUser executes pushPowerButton(), the Façade kicks in and execute the bootup operation. This is basically all the end user will ever see. Behind the scenes, each subsystem which is represented by a class get initiated and takes care of its purpose.

To create objects for each subsystem as showed above, is called Composition. Also, it is clear that all objects are loosely coupled to each other, this ensures maintainability of your program.

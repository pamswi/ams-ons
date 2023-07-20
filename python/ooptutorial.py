from abc import ABC, abstractmethod

# using abstraction a bit of polymorphism

# first superclass
class Bird(ABC):
    fly =True
    babies =0

    def noise(self):
        return "squawk"
    
    def reproduce(self):
        self.babies += 1
    
    def eat(self):
        pass

    extinct = False


# first subclass 

# we use polymorphism to override the reproduce method
# we use abstraction with the eat method
# we use inheritance as a child class

class Owl(Bird):

    def reproduce(self):
        self.babies +=6

    def eat(self):
        return "peck peck"
    
# second subclass

# we use polymorphism to override the reproduce method and fly and extinct variables
# we use encapsulation to keep the babies variable from being directly accessed
# we use inheritance again to create a child class of Bird

class Dodo(Bird):
    Fly = False
    extinct = True

    def eat(self):
        return "nom nom"
    
    def reproduce(self):
        if not self.extinct:
            self.babies += 1
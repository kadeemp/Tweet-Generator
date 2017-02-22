# Copy your Animal class here and modify it to automatically count population
# Hint: Modify the initializer method to count the number of animals created

class Animal(object):
       # A variable to count population
    population = 0

    # Implement the populationCount class method here
    @classmethod
    def populationCount(cls):
        return population.cls

    def __init__(self, name, favoriteFood):
        self.name = name
        self.favoriteFood = favoriteFood
        Animal.population += 1


    def eat(self, food):
        print self.name + " eats " + food
        if food == self.favoriteFood:
            print "YUM! " + self.name + " wants more " + food
# Copy your Tiger class here
class Tiger(Animal):
    def __init__(self, name):
        super(Tiger, self).__init__(name,"meat")


    def sleep(self):
        print (self.name + " sleeps for 8 hours" )



# Copy your Bear class here
class Bear(Animal):
    def __init__(self, name):
        super(Bear, self).__init__(name,"fish")

    def sleep(self):
        print (self.name + " hibernates for 4 months" )



# Implement the Unicorn class here as a subclass of Animal
# Hint: Implement the initializer method and override the sleep method
class Unicorn(Animal):
    def __init__(self, name):
       super(Unicorn, self).__init__(name,"marshmallows")

    def sleep(self):
        print (self.name + " sleeps in a cloud" )



# Implement the Giraffe class here as a subclass of Animal
# Hint: Implement the initializer method and override the eat method
class Giraffe(Animal):
    def __init__(self, name):
       super(Giraffe, self).__init__(name,"leaves")

    def sleep(self):
        print (self.name + " sleeps for 8 hours" )

    def eat(self, food):
        print self.name + " eats " + food
        if food == self.favoriteFood:
            print "YUM! " + self.name + " wants more " + food

        else:
            print "YUCK! " + self.name + " spits out " + food
# Implement the Bee class here as a subclass of Animal
# Hint: Implement the initializer method and override the sleep and eat methods
class Bee(Animal):
    def __init__(self, name):
       super(Bee, self).__init__(name,"honey")

    def sleep(self):
        print (self.name + " never sleeps" )

    def eat(self, food):
        print self.name + " eats " + food
        if food == self.favoriteFood:
            print "YUM! " + self.name + " wants more " + food

        else:
            print "YUCK! " + self.name + " spits out " + food
# Implement the Zookeeper class here
class Zookeeper(object):

    # Implement the initializer method here
    def __init__(self, name):
        self.name = name

    # Implement the feedAnimals method here
    def feedAnimals(self, animals, food):
        print self.name + " is feeding " + food + " to " + str(len(animals))  + " of "+ str(Animal.population)  + " total animals"

        for animal in animals:
            animal.eat(food)
            animal.sleep()

# CLASSES PUBLIC VARIABLES
# Declare a class named 'Car' which takes variables as public Name, Type, ModelNumber in the constructor
class Car:
    def __init__(self, Name, Type, ModelNumber):
        self.Name = Name
        self.Type = Type
        self.ModelNumber = ModelNumber


# Create an instance of Car with Name as 'Ferrari', Type as 'La Ferrari' and ModelNumber as 'LAF69'
myCar = Car('Ferrari', 'La Ferrari', 'LAF69')


# You can also change the values of the instance myCar as follows
myCar.ModelNumber = "F150"


# Output the car details in console with the following format
# Name Ferrari
# Type La Ferrari
# ModelNumber LAF69
print('Name', myCar.Name)
print('Type', myCar.Type)
print('ModelNumber', myCar.ModelNumber)


print("\n-----------------------------------\n")


# CLASSES PRIVATE VARIABLES
# Declare a class named 'Car' which takes variables as private Name, Type in the constructor
# Initialises AnimalID to 804564
# Include the getters and setters of each
class Animal:
    def __init__(self, Name, Type):
        self.__Name = Name
        self.__Type = Type
        self.__AnimalID = 804564

    def getName(self):
        return self.__Name

    def getType(self):
        return self.__Type

    def getAnimalID(self):
        return self.__AnimalID

    def setName(self, Name):
        self.__Name = Name

    def setType(self, Type):
        self.__Type = Type

    def setAnimalID(self, AnimalID):
        self.__AnimalID = AnimalID


# Create an instance of Animal with name as Dog and Type as Mammal
myAnimal = Animal('Dog', 'Mammal')


# Change the AnimalID to 567054
myAnimal.setAnimalID(567054)


# Output the animal details in console with the following format
# Name Dog
# Type Mammal
# AnimalID 567054

print('Name', myAnimal.getName())
print('Type', myAnimal.getType())
print('AnimalID', myAnimal.getAnimalID())


print("\n-----------------------------------\n")


# CLASS INHERITANCE
# Declare a class named 'Rect' which takes variables as private length, width in the constructor
class Rect:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def getLength(self):
        return self.__length

    def getWidth(self):
        return self.__width

    def setLength(self, length):
        self.__length = length

    def setWidth(self, width):
        self.__width = width


# Declare a class named 'Area' which takes variables as
# private length, width in the constructor. Make it inherit from class Rect.
# Include a method getArea() to calculate the area
class Area(Rect):
    def __init__(self, length, width):
        super().__init__(length, width)

    def getArea(self):
        return self.getLength() * self.getWidth()


# Declare a class named 'Volume' which takes variables as
# private length, width and height in the constructor. Make it inherit from class Rect.
# Include a method getHeight()
# Include a method getVolume() to calculate the volume
class Volume(Rect):
    def __init__(self, length, width, height):
        self.__height = height
        super().__init__(length, width)

    def getHeight(self):
        return self.__height

    def getVolume(self):
        return self.getLength() * self.getWidth() * self.getHeight()


# Print Area and Volume
area = Area(10, 10)
volume = Volume(10, 10, 10)

print('Area', area.getArea())
print('Volume', volume.getVolume())

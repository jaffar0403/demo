class Dog:
    def __init__(self, name, age):
        # Constructor to initialize the name and age of the dog
        self.name = name
        self.age = age

    def bark(self):
        # Method to make the dog bark
        return f"{self.name} says woof!"

    def get_age(self):
        # Method to get the age of the dog
        return f"{self.name} is {self.age} years old."
    def demo(self):
        print("demo testing")

    def age(self):
        print(self.age)
    def height(self):
        print("Testing")




# Create an instance of the Dog class
my_dog = Dog("Buddy", 3)
d=Dog("remo",3)
#d.age()
d.height()

# Call the methods
print(my_dog.bark())       # Output: Buddy says woof!
print(my_dog.get_age())    # Output: Buddy is 3 years old.
print(d.get_age())
d.demo()


class Animal:
    def __init__(self,AnimalType,sound):
        self.AnimalType = AnimalType
        self.sound = sound

    def details(self):
        print(f"Animal type is {self.AnimalType}")
        print(f"{self.AnimalType}'s sound is {self.sound}")

Cow = Animal("Cow","Hambaaaa")
Cow.details()

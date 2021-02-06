class Animals:
    def __init__(self, name, age, gender, species, color, number_of_feet, natural_habitat, animal_nutrition):
        self.name = name
        self.age = age
        self.gender = gender
        self.species = species
        self.color = color
        self.number_of_feet = number_of_feet
        self.natural_habitat = natural_habitat
        self.animal_nutrition = animal_nutrition

    def eat(self):
        print(self.name, "ate the", self.animal_nutrition)

    def wants_love(self):
        print(self.name, "wants to be loved.")


class Cats(Animals):
    def __init__(self, name, age, gender, species, color, number_of_feet, natural_habitat, animal_nutrition):
        super().__init__(name, age, gender, species, color, number_of_feet, natural_habitat, animal_nutrition)

    def mew(self):
        print(self.name, "wants to eat..")
        Animals.eat(self)

    def rolling(self):
        print(self.name, "throw herself on the ground..")
        Animals.wants_love(self)


class Dogs(Animals):
    def __init__(self, name, age, gender, species, color, number_of_feet, natural_habitat, animal_nutrition):
        super().__init__(name, age, gender, species, color, number_of_feet, natural_habitat, animal_nutrition)

    def bark(self):
        print(self.name, "is barking to new guests")
        Animals.wants_love(self)


if __name__ == '__main__':
    cat = Cats("Luna", 1, "female", "british", "grey", 4, "home", "cat food")
    dog = Dogs("Artemis", 3, "female", "Saint Bernard", "black", 4, "home", "beef")
    cat.mew()
    print("\n")
    dog.bark()
    print("\n")
    cat.rolling()

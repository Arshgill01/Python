class Student:  ## Methods are used in a class, to define parameters, basically a method is just a function inside of a class
    def __init__(self, name, house):

        self.name = name  ## defining instance variable
        self.house = house  ## defining instance variable

    def __str__(self):
        return f"{self.name} from {self.house}"

    # TODO: Getter
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name

    @property
    def house(self):
        return self._house

    # TODO: Setter
    @house.setter
    def house(self, house):
        if house not in ["Berlin", "Munich", "Dresden", "Frankfurt"]:
            raise ValueError("Invalid house")
        self._house = house


def main():
    student = get_student()

    print(student)


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)  # TODO: construtor call!


# use () for tuples, if you don't want any change, as you KNOW they're .....


if __name__ == "__main__":
    main()

class Plant:
    def __init__(self, name: str, height: float, age: int):
        self._name = name
        self._height = height
        self._age = age

    def set_height(self, value) -> None:
        if value < 0:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = value

    def set_age(self, value) -> None:
        if value < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = value

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def show(self) -> None:
        print(f"{self._name}: {float(self._height)}cm, {self._age} days old")

    def age(self, count: int = 1) -> None:
        self._age += count

    def grow(self, count: int = 1) -> None:
        self._height += count


class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self._color = color
        self._bloom = False

    def bloom(self) -> None:
        self._bloom = True

    def show(self) -> None:
        super().show()
        print("Color:", self._color)
        if self._bloom:
            print(f"{self._name} is blooming beautifully!")
        else:
            print(f"{self._name} has not bloomed yet")


class Tree(Plant):
    def __init__(self, name, height, age, diameter):
        super().__init__(name, height, age)
        self._diameter = diameter
        self._shade = False

    def produce_shade(self) -> None:
        print(f"Tree {self._name} now produces a ", end="")
        print(f"shade of {self._height}cm long and {self._diameter}cm wide.")

    def show(self) -> None:
        super().show()
        print("Trunk diameter:", self._diameter)


class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season):
        super().__init__(name, height, age)
        self._harvest_season = harvest_season
        self._nutritional_value = 0

    def grow(self, count: int = 1) -> None:
        for i in range(count):
            super().grow()
            self._nutritional_value += 1

    def age(self, count: int = 1) -> None:
        for i in range(count):
            super().age()

    def show(self) -> None:
        super().show()
        print("Harvest season:", self._harvest_season)
        print("Nutritional value:", self._nutritional_value)


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    rose = Flower("Rose", 15, 60, "red")
    print("=== Flower")
    rose.show()
    rose.bloom()
    rose.show()
    oak = Tree("Oak", 250, 270, 5)
    print("=== Tree")
    oak.show()
    oak.produce_shade()
    tomato = Vegetable("Tomato", 30, 70, "April")
    print("=== Vegetable")
    tomato.show()
    tomato.grow(20)
    tomato.age(20)
    tomato.show()

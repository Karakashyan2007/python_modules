class Plant:
    class Stats:
        def __init__(self):
            self.grow_count = 0
            self.age_count = 0
            self.show_count = 0

        def display(self) -> None:
            print(f"Stats: {self.grow_count} grow, "
                  f"{self.age_count} age, {self.show_count} show")

    def __init__(self, name: str, height: float, age: int):
        self._name = name
        self._height = height
        self._age = age
        self._stats = Plant.Stats()

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
        self._stats.show_count += 1

    def age(self, count: int = 1) -> None:
        self._age += count
        self._stats.age_count += count

    def grow(self, count: int = 1) -> None:
        self._height += count
        self._stats.grow_count += count

    @staticmethod
    def is_older_than_year(age: int) -> bool:
        return age > 365

    @classmethod
    def create_anonymous(cls):
        return cls("Unknown plant", 0.0, 0)


class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self._color = color
        self._bloom = False

    def bloom(self) -> None:
        self._bloom = True

    def age(self, count: int = 1) -> None:
        for i in range(count):
            super().age()

    def grow(self, count: int = 1) -> None:
        for i in range(count):
            super().grow()

    def show(self) -> None:
        super().show()
        print("Color:", self._color)
        if self._bloom:
            print(f"{self._name} is blooming beautifully!")
        else:
            print(f"{self._name} has not bloomed yet")


class Tree(Plant):
    class TreeStats(Plant.Stats):
        def __init__(self):
            super().__init__()
            self.shade_count = 0

        def display(self) -> None:
            print(f"Stats: {self.grow_count} grow, "
                  f"{self.age_count} age, {self.show_count} show")
            print(f"{self.shade_count} shade")

    def __init__(self, name, height, age, diameter):
        super().__init__(name, height, age)
        self._stats:    Tree.TreeStats = Tree.TreeStats()
        self._diameter = diameter
        self._shade = False

    def produce_shade(self) -> None:
        print(f"Tree {self._name} now produces a ", end="")
        print(f"shade of {self._height}cm long and {self._diameter}cm wide.")
        self._stats.shade_count += 1

    def show(self) -> None:
        super().show()
        print("Trunk diameter:", self._diameter)


class Seed(Flower):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age, color)
        self._seed_count = 0

    def grow(self, count: int = 1) -> None:
        super().grow(count)

    def age(self, count: int = 1) -> None:
        super().age(count)

    def bloom(self) -> None:
        super().bloom()
        self._seed_count = 42

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self._seed_count}")


def display_stats(plant) -> None:
    print(f"[statistics for {plant._name}]")
    plant._stats.display()


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    rose = Flower("Rose", 15, 60, "red")
    print("=== Flower")
    rose.show()
    display_stats(rose)
    rose.bloom()
    rose.age(1)
    rose.grow(15)
    rose.show()
    display_stats(rose)
    oak = Tree("Oak", 250, 270, 5)
    print("=== Tree")
    oak.show()
    display_stats(oak)
    oak.produce_shade()
    display_stats(oak)
    sunfl = Seed("Sunflower", 30, 70, "Yellow")
    print("=== Seed")
    sunfl.show()
    sunfl.grow(20)
    sunfl.age(20)
    sunfl.bloom()
    sunfl.show()
    display_stats(sunfl)
    print("=== Anonymous")
    anon = Plant.create_anonymous()
    anon.show()
    display_stats(anon)

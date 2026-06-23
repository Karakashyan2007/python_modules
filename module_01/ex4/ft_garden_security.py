class Plant:
    def __init__(self, name: str, height: float, age: int):
        self._init = True
        self.name = name
        self._height = 0.0
        self._age = 0
        self.set_height(height)
        self.set_age(age)
        print("Plant created:", self.show())
        self._init = False

    def set_height(self, value):
        if value >= 0:
            self._height = value
            if not self._init:
                print(f"Height updated: {self._height}cm")
        else:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")

    def set_age(self, value):
        if value >= 0:
            self._age = value
            if not self._init:
                print(f"Age updated: {self._age} days")
        else:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")

    def get_height(self):
        return self._height

    def get_age(self):
        return self._age

    def show(self):
        return f"{self.name}: {float(self._height)}cm, {self._age} days old"


if __name__ == "__main__":
    print("=== Garden Security System ===")
    plant1 = Plant("Rose", 15, 10)
    plant1.set_height(25)
    plant1.set_age(18)
    plant1.set_height(-99)
    plant1.set_age(-1)
    print("Current state:", plant1.show())

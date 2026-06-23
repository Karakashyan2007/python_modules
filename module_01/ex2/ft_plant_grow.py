class Plant:
    name: str
    height: float
    days: int

    def show(self):
        print(f"{self.name}: {self.height}cm, {self.days} days old")

    def grow(self):
        self._height += 0.8
        self._height = round(self.height, 1)

    def age(self):
        self._days += 1


if __name__ == "__main__":
    print("=== Garden Plant Growth ===")
    plant1 = Plant()
    plant1.name = "Rose"
    plant1.height = 60.0
    plant1.days = 50

    i = 1
    plant1.show()
    for i in range(1, 8):
        print(f"=== Day {i} ===")
        plant1.grow()
        plant1.age()
        plant1.show()
        i += 1

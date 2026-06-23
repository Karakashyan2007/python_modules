class Plant:
    def __init__(self, name: str, height: float, days: int):
        self.name = name
        self.height = height
        self.days = days

    def show(self):
        return f"{self.name}: {self.height}cm, {self.days} days old"


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    plant1 = Plant("Rose", 60, 50)
    plant2 = Plant("Lavender", 30, 55)
    plant3 = Plant("Orchid", 22, 33)
    plant4 = Plant("Daisy", 15, 10)
    plant5 = Plant("Lily", 40, 30)
    print("Created:", plant1.show())
    print("Created:", plant2.show())
    print("Created:", plant3.show())
    print("Created:", plant4.show())
    print("Created:", plant5.show())

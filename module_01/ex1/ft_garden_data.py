class Plant:
    name: str
    height: int
    days: int

    def show(self):
        print(f"{self.name}: {self.height}cm, {self.days} days old")


if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    plant1 = Plant()
    plant1.name = "Rose"
    plant1.height = 60
    plant1.days = 50

    plant2 = Plant()
    plant2.name = "Lavender"
    plant2.height = 30
    plant2.days = 55

    plant3 = Plant()
    plant3.name = "Orchid"
    plant3.height = 22
    plant3.days = 33
    plant1.show()
    plant2.show()
    plant3.show()

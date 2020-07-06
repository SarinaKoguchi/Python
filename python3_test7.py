class Vehicle:
    def __init__(self, name, tool, method):
        self.name = name
        self.tool = tool
        self.method = method

    def move_on(self):
        print(f"{self.name}は{self.tool}を{self.method}と進みます。")

class Car(Vehicle):
    pass

class Bicycle(Vehicle):
    pass

class Ship(Vehicle):
    pass

class Airplane(Vehicle):
    pass

car = Car("車", "アクセル", "踏む")
bicycle = Bicycle("自転車", "ペダル", "漕ぐ")
ship = Ship("船", "スクリュー", "回す")
airplane = Airplane("飛行機", "プロペラ", "回す")

car.move_on()
bicycle.move_on()
ship.move_on()
airplane.move_on()
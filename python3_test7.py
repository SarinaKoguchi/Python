from abc import ABCMeta, abstractmethod

class Vehicle(metaclass=ABCMeta):
    def __init__(self, name, tool, method):
        self.name = name
        self.tool = tool
        self.method = method

    @abstractmethod
    def move_on(self):
        pass

class Car(Vehicle):
    def move_on(self):
        print(f"{self.name}は{self.tool}を{self.method}と進みます。")

class Bicycle(Vehicle):
    def move_on(self):
        print(f"{self.name}は{self.tool}を{self.method}と進みます。")

class Ship(Vehicle):
    def move_on(self):
        print(f"{self.name}は{self.tool}を{self.method}と進みます。")

class Airplane(Vehicle):
    def move_on(self):
        print(f"{self.name}は{self.tool}を{self.method}と進みます。")

car = Car("車", "アクセル", "踏む")
bicycle = Bicycle("自転車", "ペダル", "漕ぐ")
ship = Ship("船", "スクリュー", "回す")
airplane = Airplane("飛行機", "プロペラ", "回す")

car.move_on()
bicycle.move_on()
ship.move_on()
airplane.move_on()
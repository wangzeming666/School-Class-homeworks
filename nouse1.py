class Car:
    def __init__(self):
        self.color = 'Write'
        self.model = 'A186'
        self.brand = 'blahblah'

    def run(speed):
        print(self.color, self.model, speed)

    def infos(self):
        print(self.__dict__)

    def change_color(c):
        self.color = c

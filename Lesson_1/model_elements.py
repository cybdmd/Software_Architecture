class Texture:
    pass


class Poligon:
    def __init__(self, point):
        self.point = point


class PoligonalModel:
    def __init__(self, poligon, texture):
        self.poligon = poligon
        self.texture = texture


class Scene:
    def __init__(self, idd, model, flash):
        self.idd = idd
        self.model = model
        self.flash = flash

    def method_1(self, x):
        return self.idd

    def method_2(self):
        return self.flash


class Flash:
    def __init__(self, location, angle, color, power):
        self.location = location
        self.angle = angle
        self.color = color
        self.power = power

    def rotate(self, x):
        self.angle += x

    def move(self, x):
        self.location += x


class Camera:
    def __init__(self, location, angle):
        self.location = location
        self.angle = angle

    def rotate(self, x):
        self.angle += x

    def move(self, x):
        self.location += x

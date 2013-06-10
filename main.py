import itertools
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Line, Ellipse
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.properties import (
    AliasProperty,
    NumericProperty,
    ReferenceListProperty,
    ObjectProperty
)

def to_points(tuples):
    """
    list of tuples to single list
    """
    return [element for tupl in tuples for element in tupl]

class Ball(Widget):
    speed = NumericProperty(1)
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)
    target_x = NumericProperty(0)
    target_y = NumericProperty(0)
    target = ReferenceListProperty(target_x, target_y)

    def __init__(self, *args, **kw):
        self._path = None
        super(Ball, self).__init__(*args, **kw)

    def get_path(self):
        return self._path

    def set_path(self, path):
        self._path = path
        self.center = self._path.next()
        self.set_new_target(*self._path.next())

    path = AliasProperty(get_path, set_path)

    def move(self):
        self.center = Vector(*self.velocity) + self.center
        distance = Vector(self.center).distance(self.target)
        if distance <= Vector(*self.velocity).length():
            self.set_new_target(*self.path.next())

    def set_new_target(self, x, y):
        self.target = x, y
        v = Vector(self.target) - Vector(self.center)
        self.velocity = v.normalize() * self.speed

class MainFrame(Widget):
    ball1 = ObjectProperty(None)
    ball2 = ObjectProperty(None)

    def __init__(self, *args, **kw):
        self.star7_3 = list(self.get_poligon(7, 3, 125, 125, 125))
        self.star12_5 = list(self.get_poligon(12, 5, 500, 200, 200, 180 - 360.0/12))
        self.star7_3_points = to_points(self.star7_3)
        self.star12_5_points = to_points(self.star12_5)
        super(MainFrame, self).__init__(*args, **kw)
        self.ball1.path = itertools.cycle(self.star12_5[:-1])
        self.ball2.path = itertools.cycle(list(self.get_poligon(48, 1, 500, 200, 200))[:-1])

    def update(self, dt):
        self.ball1.move()
        self.ball2.move()

    @staticmethod
    def get_poligon(vertices, density, center_x, center_y, radius, angle=None):
        """
            Returns coordinates of star poligon:
            (x1, y1), (x1, y2), ...
        """
        v = Vector(0, radius)
        if angle:
            v = v.rotate(angle)
        for i in xrange(vertices+1):
            v = v.rotate(-float(360)/vertices * density)
            yield v.x + center_x, v.y + center_y


class StarsApp(App):

    def build(self):
        main_frame = MainFrame()
        Clock.schedule_interval(main_frame.update, 1.0 / 15)
        return main_frame

if __name__ == '__main__':
    StarsApp().run()

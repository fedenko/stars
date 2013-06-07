from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Line, Ellipse
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.properties import (
    NumericProperty,
    ReferenceListProperty,
    ObjectProperty
)


class Ball(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def move(self):
        self.velocity = Vector(*self.velocity).rotate(1)
        self.pos = Vector(*self.velocity) + self.pos


class MainFrame(Widget):
    ball = ObjectProperty(None)

    def serve_ball(self, vel=(2, 0)):
        self.ball.center = self.center
        self.ball.velocity = vel

    def update(self, dt):
        self.ball.move()

    @staticmethod
    def star(vertices, density, center_x, center_y, radius, angle=None):
        v = Vector(0, radius)
        if angle:
            v = v.rotate(angle)
        points = []
        for i in xrange(vertices+1):
            v = v.rotate(float(360)/vertices * density)
            points.append(int(v.x) + center_x)
            points.append(int(v.y) + center_y)
        return points


class StarsApp(App):

    def build(self):
        main_frame = MainFrame()
        main_frame.serve_ball()
        Clock.schedule_interval(main_frame.update, 1.0 / 24)
        return main_frame

if __name__ == '__main__':
    StarsApp().run()

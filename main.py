from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Line
from kivy.vector import Vector

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


class MainFrame(Widget):
    def __init__(self, *args, **kw):
        super(MainFrame, self).__init__(*args, **kw)
        with self.canvas:
            Color(1, 1, 1)
            Line(points=star(7, 3, 125, 125, 125))
            Line(circle=(125, 125, 125))
            Line(points=star(12, 5, 500, 125, 125))
            Line(circle=(500, 125, 125))


class StarsApp(App):

    def build(self):
        return MainFrame()

if __name__ == '__main__':
    StarsApp().run()

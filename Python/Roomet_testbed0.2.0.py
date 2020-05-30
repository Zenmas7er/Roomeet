from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.colorpicker import ColorPicker
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.stencilview import StencilView
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse, Line, Rectangle
from kivy.properties import ListProperty, ObjectProperty
from random import random as r

col = [1, 1, 1, 1]

class SelectedColor(Widget):
    selected_color = ListProperty(col)

class RoomeetCanvas(StencilView):
    def on_touch_down(self, touch):
        with self.canvas:
            sce = SelectedColor()
            sce.center = touch.pos
            self.add_widget(sce)

            touch.ud['line'] = Line(points=(touch.x, touch.y),
                                    width=int(2))

    def on_touch_move(self, touch):
        if 'line' in touch.ud:
            touch.ud['line'].points += [touch.x, touch.y]

class Roomeet020App(App):

    '''The section of code that
        builds the Kivy application'''
    def build(self):
        wid = RoomeetCanvas(size_hint = (None, None), size = Window.size)

        btn_penSize = Button(text = 'Pen Size')

        btn_color = Button(text = 'Select Color')

        btn_eraser = Button(text = 'Eraser')

        btn_exportPNG = Button(text = 'Save as .PNG')

        layout = BoxLayout(size_hint = (1, None), height = 25)
        layout.add_widget(btn_penSize)
        layout.add_widget(btn_color)
        layout.add_widget(btn_eraser)
        layout.add_widget(btn_exportPNG)

        root = BoxLayout(orientation = 'vertical')
        board = FloatLayout()
        board.add_widget(wid)
        root.add_widget(board)
        root.add_widget(layout)

        return root

if __name__ == '__main__':
    Roomeet020App().run()

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.colorpicker import ColorPicker
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.stencilview import StencilView
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse, Line, Rectangle
from kivy.properties import ListProperty, ObjectProperty

from functools import partial
from random import random as r

col = [1, 1, 1, 1]

class SelectedColor(Widget):
    selected_color = ListProperty(col)

class RoomeetCanvas(StencilView):
    selected_color = ListProperty(col)

    def on_touch_down(self, touch):
        with self.canvas:
            penColor = SelectedColor()
            penColor.selected_color = self.selected_color
            print('penColor.selected_color is ', penColor.selected_color)
            penColor.center = touch.pos
            self.add_widget(penColor)

            touch.ud['line'] = Line(points=(touch.x, touch.y),
                                    width=int(2))

    def on_touch_move(self, touch):
        if 'line' in touch.ud:
            touch.ud['line'].points += [touch.x, touch.y]

class Roomeet020App(App):
    
    def color_picker(self, wid, btn_color):

        colPckr = ColorPicker()
        
        select_button = Button(text = "Select", size = (100, 25))
        layout = GridLayout(cols = 1, padding = 10)

        layout.add_widget(select_button)
        layout.add_widget(colPckr)

        color_popup = Popup(title = 'Color Wheel', content = layout,
                            size_hint = (None, None), size = (600, 600))
        color_popup.open()

        # To monitor changes, we can bind to color property changes
        def on_color(instance, value):
            print ("RGBA = ", str(value))  #  or instance.color
            print ("HSV = ", str(instance.hsv))
            print ("HEX = ", str(instance.hex_color))

            global col
            col = value
            wid.selected_color = value

        colPckr.bind(color = on_color)
        select_button.bind(on_press = color_popup.dismiss)

    '''The section of code that
        builds the Kivy application'''
    def build(self):
        wid = RoomeetCanvas(size_hint = (None, None), size = Window.size)

        btn_penSize = Button(text = 'Pen Size')

        btn_color = Button(text = 'Select Color')
        btn_color.bind(on_press = partial(self.color_picker, wid))

        btn_eraser = Button(text = 'Clear')

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

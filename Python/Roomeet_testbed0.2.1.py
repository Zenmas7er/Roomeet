from kivy.app import App
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
from kivy.utils import get_color_from_hex
from kivy.input.providers import wm_pen

from functools import partial
from random import random as r

col = [0, 0, 0, 1]

class SelectedColor(Widget):
    selected_color = ListProperty(col)

class ColPckr(ColorPicker):
    pass

class ColPopup(Popup):
    pass

# This is the "main" function of the app
class RoomeetCanvas(FloatLayout, StencilView):
    fileName = ObjectProperty(None)
    selected_color = ListProperty(col)
    
    # Allows a popup with the color picker to show up
    def select_ColPckr(self,*args):
        ColPopup().open()

    def select_Clear(self):
        with self.canvas:
            saved = self.children[:]
            self.clear_widgets()
            for widget in saved:
                self.add_widget(widget)

    def on_touch_down(self, touch):
        toggleBool = False
        # if-statement prevents user from drawing on the buttons
        if touch.x < 2000 and touch.y > 700:
            return super(RoomeetCanvas, self).on_touch_down(touch)

        if toggleBool:
            self.pos = touch.pos
            self.size = (1, 1)

        # Starts the drawing process
        with self.canvas:
            sce = SelectedColor()
            sce.selected_color = self.selected_color
            sce.center = touch.pos
            self.add_widget(sce)

            touch.ud['line'] = Line(points=(touch.x, touch.y),
                                    width=int(2))

    def on_touch_move(self, touch):
        toggleBool = False

        # if-statement prevents user from drawing on the buttons
        if touch.x < 2000 and touch.y > 700:
            return super(RoomeetCanvas, self).on_touch_move(touch)

        if toggleBool:
            self.size = (touch.x - touch.ox, touch.y - touch.oy)

        # Continues the drawing process
        if 'line' in touch.ud:
            touch.ud['line'].points += [touch.x, touch.y]

    # Functions allows the user to save a .png file of the canvas
    def select_savePNG(self):
        text = self.fileName.text
        self.export_to_png(text + '.png')

# The section of code that builds the Kivy application
class Roomeet021App(App):
    def build(self):
        return RoomeetCanvas()

if __name__ == '__main__':
    Window.clearcolor = get_color_from_hex('#FFFFFF')
    Roomeet021App().run()

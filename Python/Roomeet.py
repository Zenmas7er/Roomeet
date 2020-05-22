from kivy.app import App
from kivy.uix.popup import Popup
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.colorpicker import ColorPicker
from kivy.graphics import Color, Line
from kivy.properties import ListProperty, ObjectProperty
col = [0, 0, 1, 1]

class SelectedColor(Widget):
    selected_color = ListProperty(col)

class ColPckr(ColorPicker):
    pass

class ColPopup(Popup):
    pass

class RoomeetWidget(Widget):
    penSlider = ObjectProperty(None)
    fileName = ObjectProperty(None)
    selected_color = ListProperty(col)
    
    def select_ColPckr(self,*args):
        ColPopup().open()

    def on_touch_down(self, touch):
        if touch.x < 1000 and touch.y < 200:
            return super(RoomeetWidget, self).on_touch_down(touch)
        with self.canvas:
            sce = SelectedColor()
            sce.selected_color = self.selected_color
            sce.center = touch.pos
            self.add_widget(sce)

            touch.ud['line'] = Line(points=(touch.x, touch.y),
                                    width=int(self.penSlider.value))

    def on_touch_move(self, touch):
        if 'line' in touch.ud:
            touch.ud['line'].points += [touch.x, touch.y]

    def select_savePNG(self):
        text = self.fileName.text
        self.export_to_png(text + '.png')

class RoomeetApp(App):
    def build(self):
        return RoomeetWidget()


if __name__ == '__main__':
    RoomeetApp().run()

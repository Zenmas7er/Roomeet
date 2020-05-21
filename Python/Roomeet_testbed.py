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

class MyPaintWidget(Widget):
    penSlider = ObjectProperty(None)
    selected_color = ListProperty(col)
    
    def select_ColPckr(self,*args):
        ColPopup().open()
    
    def select_Clear(self):
        saved = self.children[:]
        self.clear_widgets()
        self.canvas.clear()
        for widget in saved:
            self.add_widget(widget)
    
    def on_touch_down(self, touch):
        if touch.x < 400 and touch.y < 200:
            return super(MyPaintWidget, self).on_touch_down(touch)
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
        text = self.ids.fileName.text
        self.export_to_png(text + '.png')

class MyPaintApp(App):
    def build(self):
        return MyPaintWidget()


if __name__ == '__main__':
    MyPaintApp().run()

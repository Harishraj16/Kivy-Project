from kivy.app import App
from kivy.metrics import dp
from kivy.properties import StringProperty, BooleanProperty
from kivy.uix import widget
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.widget import Widget


class WidgetExample(GridLayout):
    my_text = StringProperty("1")
    count = 1
    slider_txt = StringProperty("value")
    count_enabled = BooleanProperty(False)
    switch_enabled = BooleanProperty(False)

    def on_button_click(self):
        if self.count_enabled:
            print("Button Clicked")
            self.count += 1
            self.my_text = "{}".format(self.count)

    def on_toogle_button_state(self, widget):
        print("toggle start: " + widget.state)
        if widget.state == "normal":
            widget.text = "OFF"
            self.count_enabled = False
        else:
            widget.text = "ON"
            self.count_enabled = True

    def on_switch_state(self, widget):
        print("Switch: " + str(widget.active))
        # widget.active value is a boolean so enclose in str()

    #def on_slider_value(self, widget):
        #print("Slider: " + str(int(widget.value)))
        #self.slider_txt = str(int(widget.value))


class StackLayoutExample(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "lr-tb"
        for i in range(0, 100):
            # size = dp(100)+i*10
            size = dp(100)
            b = Button(text=str(i + 1), size_hint=(None, None), size=(size, size))
            self.add_widget(b)


# class GridLayoutExample(GridLayout):
#    pass

class AnchorLayoutExample(AnchorLayout):
    pass


class BoxLayoutExample(BoxLayout):
    pass


""" 
    def __init__(self  , **kwargs):
        super().__init__(**kwargs)
        self.orientation = ""
        b1 = Button(text="A")
        b2 = Button(text="B")
        b3 = Button(text="C")

        self.add_widget(b1)
        self.add_widget(b2)
        self.add_widget(b3)
"""


class MainWidget(Widget):
    pass


class TheLabApp(App):
    pass


TheLabApp().run()

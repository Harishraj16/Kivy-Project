from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class MainScreen(Screen):
    pass

class Page1(Screen):
    pass

class Page2(Screen):
    pass

class Page3(Screen):
    pass

class ButtonBar(BoxLayout):
    def __init__(self, **kwargs):
        super(ButtonBar, self).__init__(**kwargs)
        self.orientation = 'horizontal'
        self.size_hint_y = None  # Ensure fixed height
        self.height = 50  # Set the height of the button bar

        # Add buttons with different screen names as arguments
        self.add_widget(Button(text="Page 1", on_press=self.change_screen_page1))
        self.add_widget(Button(text="Page 2", on_press=self.change_screen_page2))
        self.add_widget(Button(text="Page 3", on_press=self.change_screen_page3))

    def change_screen_page1(self, instance):
        App.get_running_app().root.current = "page1"

    def change_screen_page2(self, instance):
        App.get_running_app().root.current = "page2"

    def change_screen_page3(self, instance):
        App.get_running_app().root.current = "page3"

class TestApp(App):
    def build(self):
        # Create screen manager and add screens
        sm = ScreenManager()
        sm.add_widget(MainScreen(name="main"))
        sm.add_widget(Page1(name="page1"))
        sm.add_widget(Page2(name="page2"))
        sm.add_widget(Page3(name="page3"))

        # Create and add the button bar to the main screen
        button_bar = ButtonBar()
        MainScreen.add_widget(button_bar)

        return sm

if __name__ == '__main__':
    TestApp().run()

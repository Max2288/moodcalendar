from kivy.uix.screenmanager import FadeTransition
from kivy.uix.screenmanager import ScreenManager
from kivy.app import App
import kivy

from screens.calendar import CalendarScreen
from screens.main import MoodScreen

kivy.require("1.0.7")


class MoodApp(App):
    def build(self):
        sm = ScreenManager(transition=FadeTransition())
        sm.add_widget(MoodScreen(name="mood"))
        sm.add_widget(CalendarScreen(name="calendar"))
        sm.current = 'mood'
        return sm


if __name__ == "__main__":
    MoodApp().run()

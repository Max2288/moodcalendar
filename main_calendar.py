import kivy

kivy.require("1.0.7")

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.screenmanager import FadeTransition
from services import set, get


class ImageButton(ButtonBehavior, Image):
    def __init__(self, data:str, **kwargs):
        super().__init__(**kwargs)
        self.data = data


class MoodScreen(Screen):
    """Mood calendar."""

    current_mood = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        box = BoxLayout(
            padding=10,
            orientation="vertical",
        )
        
        box.add_widget(Label(text='Сохраните ваше настроение'))
        
        mood_box = BoxLayout(
            orientation="horizontal",
        )
        btn_good = ImageButton(
            source="./images/good.png",
            on_press=self.mood_callback,
            data="Хорошее",
        )
        btn_very_good = ImageButton(
            source="./images/very_good.png",
            on_press=self.mood_callback,
            data="Очень хорошее",
        )
        btn_bad = ImageButton(
            source="./images/bad.png",
            on_press=self.mood_callback,
            data="Плохое",
        )
        btn_very_bad = ImageButton(
            source="./images/very_bad.png",
            on_press=self.mood_callback,
            data="Очень плохое",
        )
        mood_box.add_widget(btn_good)
        mood_box.add_widget(btn_very_good)
        mood_box.add_widget(btn_bad)
        mood_box.add_widget(btn_very_bad)
        box.add_widget(mood_box)

        self.label = Label(text="Текущее настроение: не выбранно")
        box.add_widget(self.label)


        btn_save = Button(
            text="Сохранить выбранное настроение",
            
            )
        btn_calendar = Button(
            text="Открыть календарь",
            on_press=self.open_calendar,
        )
        action_box = BoxLayout(
            padding=10,
            orientation="horizontal",
        )
        action_box.add_widget(btn_save)
        action_box.add_widget(btn_calendar)
        box.add_widget(action_box)

        self.add_widget(box)

    def mood_callback(self, instance):
        print(instance.data)
        self.current_mood = instance.data
        self.label.text = "Ваше настроение: " + self.current_mood
        
    
    def open_calendar(self, instance):
        self.manager.current = 'calendar'

class CalendarScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        box = BoxLayout(padding=10, orientation='vertical')
        box.add_widget(Label(text='Календарь настроения'))
        """box_week = BoxLayout(orientation = "horizontal")
        box_week.add_widget(Label(text = get()))
        self.add_widget(box_week)"""    
        main_box = BoxLayout(orientation = "vertical")
        for week in range (5):
            week = BoxLayout(orientation ="horizontal")
            for day in range (7):
                week.add_widget(Label(text=str(day)))        
            main_box.add_widget(week)        
                
        
       
                        
        self.add_widget(main_box)        


        box.add_widget(Button(text='Назад',size_hint = (1,.3), on_press=self.open_mood))
        self.add_widget(box)

    def open_mood(self, instance):
        self.manager.current='mood'

class MoodApp(App):
    def build(self):
        sm = ScreenManager(transition=FadeTransition())
        sm.add_widget(MoodScreen(name="mood"))
        sm.add_widget(CalendarScreen(name="calendar"))
        sm.current = 'mood'
        return sm


if __name__ == "__main__":
    MoodApp().run()

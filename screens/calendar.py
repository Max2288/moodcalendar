import datetime
from services import get
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

mood_colors = {
    "Хорошее": "lightgreen",
    "Очень хорошее": "green",
    "Плохое": "yellow",
    "Очень плохое": "red",
}

month_names = {
    8: "Август"
}


class CalendarScreen(Screen):
    current_month = datetime.datetime.now().month

    def __init__(self, **kw):
        super().__init__(**kw)
        box = BoxLayout(orientation='vertical')
        box.add_widget(
            Label(text='Календарь настроения, ' + month_names[self.current_month]))
        self.main_box = BoxLayout(orientation="vertical", )
        self.reload_calendar(None)
        self.add_widget(self.main_box)

        box.add_widget(Button(text='Назад', size_hint=(
            1, .3), on_press=self.open_mood))
        box.add_widget(Button(text='Обновить', size_hint=(
            1, .3), on_press=self.reload_calendar))
        self.add_widget(box)

    def reload_calendar(self, instance):
        self.main_box.clear_widgets()
        moods = get()
        for week_num in range(5):
            week = BoxLayout(orientation="horizontal", size_hint=(None, None))
            for day in range(1, 8):
                date = f"{(day+week_num*7):02d}.{self.current_month:02d}.2022"
                try:
                    mood = moods[date]
                    color = mood_colors[mood]
                except:
                    color = "blue"
                    mood = "Не указано"
                week.add_widget(Label(text=f"{date}\n{mood}", color=color))
            self.main_box.add_widget(week)

    def open_mood(self, instance):
        self.manager.current = 'mood'

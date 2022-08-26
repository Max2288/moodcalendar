from services import set
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior


class ImageButton(ButtonBehavior, Image):
    def __init__(self, data: str, **kwargs):
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
        mood_box.add_widget(btn_very_good)
        mood_box.add_widget(btn_good)
        mood_box.add_widget(btn_bad)
        mood_box.add_widget(btn_very_bad)
        box.add_widget(mood_box)

        self.label = Label(text="Текущее настроение: не выбранно")
        box.add_widget(self.label)

        btn_save = Button(
            text="Сохранить выбранное настроение",
            on_press=self.save_mood
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

    def save_mood(self, instance):
        try:
            set(self.current_mood)
        except:
            popup = Popup(title="Ошибка",
                          content=Label(
                              text="Вы уже выбрали настроение на сегодня"),
                          size_hint=(None, None), size=(400, 400))
            popup.open()
        self.open_calendar(instance)

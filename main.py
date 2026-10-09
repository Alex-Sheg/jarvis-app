import threading
import json
import requests
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock
from plyer import tts, stt

SERVER_URL = "https://moi-server.duckdns.org/api/command"
WAKE_WORDS = ("джарвис", "jarvis", "жарвис", "джервис")

class JarvisApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=50, spacing=20)
        self.status_label = Label(text="Jarvis готов. Нажми кнопку.", font_size='20sp')
        self.listen_btn = Button(text="Слушать", font_size='24sp', size_hint=(1, 0.3))
        self.listen_btn.bind(on_press=self.start_listening)
        self.layout.add_widget(self.status_label)
        self.layout.add_widget(self.listen_btn)
        return self.layout

    def start_listening(self, instance):
        self.status_label.text = "Слушаю..."
        threading.Thread(target=self._listen_loop, daemon=True).start()

    def _listen_loop(self):
        try:
            # Plyer STT требует настройки колбэков, это упрощённый каркас
            stt.start()
            Clock.schedule_once(lambda dt: setattr(self.status_label, 'text', "Обработка..."), 0)
        except Exception as e:
            Clock.schedule_once(lambda dt, err=e: setattr(self.status_label, 'text', f"Ошибка: {err}"), 0)

    def say(self, text):
        def _speak(dt):
            tts.speak(text)
        Clock.schedule_once(_speak, 0)

if __name__ == "__main__":
    JarvisApp().run()

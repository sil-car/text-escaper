from kivy.config import Config
Config.set('graphics', 'resizable', False)
Config.set('graphics', 'width', '500')
Config.set('graphics', 'height', '125')
from kivy.app import App
from kivy.uix.widget import Widget

from esc import string_to_unicode
from esc import wordlist_to_unicode

class UniScapeWindow(Widget):
    def update_output(self):
        # self.t_output.text = string_to_unicode(self.t_input.text)
        self.t_output.text = wordlist_to_unicode(self.t_input.text.split())

class UniScapeApp(App):
    def build(self):
        return UniScapeWindow()

if __name__ == '__main__':
    UniScapeApp().run()

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config
import time

Config.set('graphics', 'Resizable', '0')
Config.set('graphics', 'width', '360')
Config.set('graphics', 'height', '800')


class CameraClick(BoxLayout):
    def capture(self):
        camera = self.ids['camera']
        timestr = time.strftime("%Y%m%d_%H%M%S")
        camera.export_to_png("IMG_" + timestr + ".png")
        print("Captured")


class TestCamera(App):
    def build(self):
        Builder.load_file("./camera.kv")
        return CameraClick()


if __name__ == '__main__':
    TestCamera().run()
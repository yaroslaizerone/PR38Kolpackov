from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager


class CameraScreen(Screen):
    pass


class MainScreen(Screen):
    pass


class ScreenManagement(ScreenManager):
    pass


class Main(App):
    def build(self):
        return Builder.load_file("camera.kv")

    def picture_taken(self):
        print("Фото сохранено!")

    def change_cam(self, instance):
        camera = instance.parent.ids.xcamera
        if camera.index == 0:
            camera.index = int(camera.index) + 1
        elif camera.index == 1:
            camera.index = int(camera.index) - 1
        else:
            camera.index = camera.index


if __name__ == "__main__":
    Main().run()

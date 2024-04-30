from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.camera import Camera
from kivy.clock import Clock
from kivy.graphics.texture import Texture
from kivy.uix.button import Button
import cv2
import numpy as np

class KivyCamera(Camera):
    def __init__(self, **kwargs):
        super(KivyCamera, self).__init__(**kwargs)
        self.capture = None
        Clock.schedule_interval(self.update, 1.0 / 30)

    def start(self):
        self.capture = cv2.VideoCapture(0)

    def stop(self):
        self.capture.release()
        Clock.unschedule(self.update)

    def update(self, dt):
        if self.capture is not None:
            ret, frame = self.capture.read()
            if ret:
                # Convert it to texture
                buf = cv2.flip(frame, 0).tostring()
                image_texture = Texture.create(
                    size=(frame.shape[1], frame.shape[0]), colorfmt='bgr'
                )
                image_texture.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
                # display image from the texture
                self.texture = image_texture

# class Mylayout(BoxLayout):
#     def __init__(self, **kwargs):
#         super(Mylayout, self).__init__(**kwargs)
#         self.word = Button(text ='Press me')
#         self.word.bind(on_press=self.button_pressed)

#         self.add_widget(self.camera)
#         self.add_widget(self.word)

#     def button_pressed(self):
#         CameraApp.on_stop()

class CameraApp(App):
    def build(self):
        self.camera = KivyCamera(play=True)
        self.word = Button(text ='Press me')
        self.word.bind(on_press=self.on_stop)

        layout = BoxLayout(orientation= 'vertical')
        layout.add_widget(self.camera)
        layout.add_widget(self.word)

        return layout

    def on_start(self):
        self.camera.start()

    def on_stop(self):
        self.camera.stop()

if __name__ == '__main__':
    CameraApp().run()
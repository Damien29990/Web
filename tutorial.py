from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.recycleview import RecycleView
from kivy.properties import ObjectProperty

class RootWidget(BoxLayout):
    count = 0

    stopbutton = ObjectProperty(None)
    numberholder = ObjectProperty(None)
    add = ObjectProperty(None)
    minus = ObjectProperty(None)

    def stop(self):
        print(self.count)
        App.get_running_app().stop()

    def increment(self):
        self.count += 1
        self.numberholder.text = str(self.count)

    def decrement(self):
        self.count -= 1
        self.numberholder.text = str(self.count)

class MyApp(App):
    def build(self):
        return RootWidget()
    
    

# if __name__ == '__main__':
MyApp().run()
import kivy
kivy.require('1.4.0')
 
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.camera import Camera
from kivy.uix.button import Button
from kivy.core.window import Window
 
class MyApp(App):
          # Function to take a screenshot
          def doscreenshot(self,*largs):
                Window.screenshot(name='screenshot%(counter)04d.jpg')
     
          def build(self):
                camwidget = Widget()  #Create a camera Widget
                cam = Camera()        #Get the camera
                cam=Camera(resolution=(640,480), size=(500,500))
                cam.play=True         #Start the camera
                camwidget.add_widget(cam)
 
                button=Button(text='screenshot',size_hint=(0.12,0.12))
                button.bind(on_press=self.doscreenshot)
                camwidget.add_widget(button)    #Add button to Camera Widget
                 
                return camwidget
             
if __name__ == '__main__':
    MyApp().run()    

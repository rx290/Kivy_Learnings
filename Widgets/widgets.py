#Importing Base App
from msilib.schema import Class
from kivy.app import  App
#Importing Widget for App
from kivy.uix.widget import Widget
#Importing Button for App
from kivy.uix.button import Button
# Importing Box Layout
from kivy.uix.boxlayout import BoxLayout
# Importing Anchor Layout
from kivy.uix.anchorlayout import AnchorLayout
# Importing Grid Layout
from kivy.uix.gridlayout import GridLayout
# Impporting Stack Layout 
from kivy.uix.stacklayout import  StackLayout
# Importing Scrollview Layout
from kivy.uix.scrollview import ScrollView
# Importing Widget properties
from kivy.properties import  StringProperty

class WidgetEnv(GridLayout):
    num = 0
    label_text = StringProperty("0")
    #Creating a button on press function to increment the number and display it as a counter
    def on_button_press(self):
        self.num += 1
        self.label_text = str(self.num)

# Base Class which is the foundation or blueprint of the entire app
class widgets(App):
    pass

#Launching the instance of the base lib
widgets().run()
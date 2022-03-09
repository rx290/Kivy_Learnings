#Importing Base App
from cgitb import text
from tkinter import Canvas
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

# Base Class which is the foundation or blueprint of the entire app
class canvas(App):
    pass

class CanvasEnv(Widget):
    pass
class CanvasEnv2(Widget):
    pass
class CanvasEnv3(Widget):
    pass


#Launching the instance of the base lib
canvas().run()


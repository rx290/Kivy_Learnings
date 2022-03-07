#Importing Base App
from cgitb import text
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

#Canvas Class to create diffrent objects and environment in the Kivy 
class MainWidget(Widget):
    pass

# Base Class which is the foundation or blueprint of the entire app
class TheLabApp(App):
    pass

#Launching the instance of the base lib
TheLabApp().run()


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

# Grid layout implementation
# Grid layout is where you can actually control everything with rows and columns drawn on the canvas i.e. screen
# we can also initiate a class with .kv file so for demonstration purposes i'm going to comment out this class and use the class there
# class GridLayoutEnv(GridLayout):
#     pass


# Anchor layout Implementation
# Anchor layout takes all space you need to place and size the widgets within it
class AnchorLayoutEnv(AnchorLayout):
    pass


# Box layout Implementation
# Change the main widget / main layout to the name of layout class defined here to implement the it
class BoxLayoutEnv(BoxLayout):
    pass
    """
    # Constructor
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Changing Orientation of the widget Placements
        self.orientation = "vertical"
        # Initializing a button
        btn = Button(text="Some Button")
        btn2 = Button(text="Weird Button")
        # Adding Button to the app canvas
        self.add_widget(btn)
        self.add_widget(btn2)
        """


#Widget Class to create diffrent objects and environment in the Kivy 
class MainWidget(Widget):
    pass

# Base Class which is the foundation or blueprint of the entire app
class TheLabApp(App):
    pass

#Launching the instance of the base lib
TheLabApp().run()


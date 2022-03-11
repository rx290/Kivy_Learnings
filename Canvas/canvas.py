#Importing Base App
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

from  kivy.graphics import *
from  kivy.metrics import *

from kivy.properties import Clock


# Base Class which is the foundation or blueprint of the entire app
class canvas(App):
    pass
  
class CanvasEnv(Widget):
    pass
class CanvasEnv2(Widget):
    pass
class CanvasEnv3(Widget):
    pass

# Adding canvas and drawing shapes with code
class CanvasEnv4(Widget):
        
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Canvas
        with self.canvas:
            # Drawing a line
            Line(points=[100,100,400,500], width=2)
            # Drawing a circle with a line
            Line(circle=[400,200,80])
            # Drawing a rectangle with a line
            Line(rectangle=[700,500,150,100])
            # Drawing a rectangle with Rectangle Object 
            self.rect= Rectangle(pos=(700,200),size=(150,100))
    def move_box(self):
        # Creating x and y position parameter for rectangle position
        x,y = self.rect.pos
        w,h = self.rect.size
        
        increment = dp(10)
        
        # Logic to make a border at the right side of the window
        rect_pos_diff = self.width - (x+w)
        if rect_pos_diff < inc:
            inc = rect_pos_diff
        # Updating the current position
        x += increment
        # As tuple are immutable we are assigning new values to the pos pram
        self.rect.pos = (x,y)

# 60 fps function
class CanvasEnv5(Widget):
        
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ball_size =dp(50)
        # Canvas
        with self.canvas:
            # Property to keep ball in center
            self.ball = Ellipse(pos=self.center, size=(self.ball_size,self.ball_size))
        # Property to call update function
        Clock.schedule_interval(self.update,1/60)
    
    # Function to move ball
    def on_size(self,*args):
        self.ball.pos = ( self.center_x - self.ball_size/2, self.center_y-self.ball_size/2 )
    
    # Function to send and update location
    def update(self, dt):
        x,y = self.ball.pos
        self.ball.pos = (x+10,y)
        
#Launching the instance of the base lib
canvas().run()


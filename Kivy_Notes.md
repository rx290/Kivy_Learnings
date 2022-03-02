# Kivy Notes

## Installation

    1. Create a virtual env by executing command "python -m virtualenv Env_name"
    2. Activate it by executing "Path_to_Kivy_env\Scripts\activate" or "source path_to_kivy_env\bin\activate"
    3. Install Kivy Library there by executing "pip install kivy" command

## Setting up the project

    1. We are using VS Code as a Code Editor
    2. In the directory of kivy_env Create a file and call it "main.py"
    3. In the bottom right of the code editor click on Python version and select the source of your Kivy_env
    4. You're good to go.

## Important Notes

    When creating the base app should be named exactly what the .kv design file is going to get named.
    Otherwise kivy GUI will show a blank screen

## Basics

    Start with a class like all other libraries.
    from kivy.app import App

    Class NameApp(App):
        pass

    Now we need components for the app don't we lets import that by creating another class and importing the required components from kivy
    from kivy.uix.widget import Widget

    class MainWidget(Widget):
        pass

    Now in the same directory create a Desired_name.kv extension file to store what graphical user interface will look like
    it has three parts:
       1. Displaying a widget.
       2. How to place a widget at some point and it's placement strategies in other words layouts.

    There are six layouts which are as follows:
        1. Box layout  
            Used for vertical and horizontal stacking of widgets
        2. Anchor layout  
            Used to put widgets at each corner of the screen
        3. Grid layout
            used to organize widget with a number of row or a number of columns
        4. Stack Layout
            used to stack items but when the spaces is occupied the widget moves to next line
        5. Scroll View
            used for a view which is greater than the view screen and can be scrolled horizontally or vertically
        6. Page layout
            It uses all the combination of all previous layout and let you view it as a book

    Other layouts:
        1. Float Layout
        2. Relative Layout
        3. Scatter Layout

### Buttons & Labels (with conf/kv file)

    Creating Buttons & Labels:
        We have to edit the .kv files
        We can use pixels and dpi to create buttons
        examples are as follows:
                    Pixels:
                        Button:
                            text: "Btn_1_wpp"
                            size:  400,200
                            pos:   100,200

                    DPI:
                        Button:
                            text: "Btn_2"
                            size:  "40dp","20dp"
                            pos:   "200dp","400dp"

        To create labels we need to change the label from button to label:
                Example:
                    Label:
                        text: "Some Text"
                        size:  "40dp","20dp"
                        pos:   "200dp","400dp"
                        color: red, green, blue, alpha(opacity)

### Layouts

    1. Box layout
    2. Anchor layout  
    3. Grid layout
    4. Stack Layout
    5. Scroll View
    6. Page layout

# The Lab Part 2

## Content

    This section is going to teach use different widgets which are as follows:
        1. Toggle Buttons
        2. Custom Fonts
        3. Button Click function & its Relation
        4. Button properties Manipulation
        5. Switch Widget
        6. Slider Widget
        7. Progress bar widget
        8. Text Input
        9. Image Widget
        10. Using properties in KV design file

### Toggle Button

    This is similar to a button but unlike a button toggle button can maintain a state.
    To use that state we use a property called on_state for example:
    on_state: root.on_state_func()

### Programmatic Variables in KV Files

    When using variables in kv files we don't use self but root as root is the base of our kivy project and it is going to access all the member of the class which inherited it.

### Button Click

    To use button click we need a property called on_press in kv designs and declare the function inside of the layout class then use it like this root.func_name()

### Custom Fonts

    To use custom font we either need to create a folder or simply place the font ttf inside of the current directory and use it with the label property of font_name like this:
    font_name: "fonts/some_font.ttf"
    
    or

    You can simply use OS default fonts like on windows we can use Arial, Comic etc

### Switch

    Switch is similar to toggle button but unlike it it manages the state and sets a trigger when it is manipulated
    example:
        Switch:
            on_active: root.on_switch_active(self)
            size_hint: None,1
            width: "80dp"

### Slider

    A simple widget which grabs continuos value be it in either horizontal or vertical orientation.
    Example:
        Slider:
            # Provide minimum value here
            min:0
            # Provide maximum value here
            max:100
            # Provide default value here
            value: 50
            # Give function which is triggered when the value is changed
            on_value: root.on_value_change(self)
            # Give orientation details here
            orientation: "vertical or horizontal"

### ID

    id is the unique attribute or property of the widget which helps us to get values out of particular widgets.
    let say if we add id to slider than we can simply get the values of the slider without the need of the on_value property.
    following scenario has been implemented in the kv file.

### ProgressBar

    A widget which displays continuity of a value without interaction.
    Minimum value can't be overridden in progressbar

### TextInput

    An input mechanism for kivy to let user feed some information to the software
    We can use this to update other widgets as well.
    This is by default multiline and can be overridden as single line input by its attributes.
    on_text_Validate can be used to update text when enter line is pressed.

### Image

    An image widget is there to place images within out app.
    properties:
        1. allow_stretch
                Useful when making a resizable widget
        2. keep_ratio
                Useful for backgrounds like gradients and other stuff

### Screen Manager

### Managing Navigation Stack
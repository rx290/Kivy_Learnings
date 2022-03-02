# The Lab

## Content

    This section is going to teach us diffrent widgets which are as follows:
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



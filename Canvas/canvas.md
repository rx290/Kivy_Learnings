# The Lab Part 3

## Content

    This section is going to teach use of a widget which is there to draw and update those drawings:
        1. Canvas
        2. Shapes
           1. Rectangle
           2. Ellipse
        3. Lines
           1. Points
           2. Rectangle
           3. Ellipse
        4. Color
        5. Movements of the shape
        6. Coordinates (Relative Layout)
        7. Page layout Backgrounds
        8. Canvas Menu

## Canvas

    The canvas is a drawing widget, which is used to draw shapes, lines and color.
    Design file Syntax:
        canvas:
            Color:
                rgb: 1,0,0
            Line:
                # POS_X, POS_Y, Radius of the Circle
                circle: (200,200,100)
                # Border Width
                width:  2.
            Line:
                ellipse: (500,300,100,200)
                width: 2.
            Rectangle:
                pos: 200,500
                size: 200,100

    Code Syntax:
        Ellipse(pos=(x,y), size=(x,y))
 
### Shapes

#### Rectangle

#### Ellipse

#### Line

#### Color


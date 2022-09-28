#import microbit 
def on_button_pressed_a():
    basic.show_number(input.compass_heading())
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_forever():
    if 360 - input.compass_heading() <= 45 and 360 - input.compass_heading() >= 0:
        basic.show_arrow(ArrowNames.NORTH_EAST)
    if 360 - input.compass_heading() <= 90 and 360 - input.compass_heading() >= 45:
        basic.show_arrow(ArrowNames.EAST)
    if 360 - input.compass_heading() <= 135 and 360 - input.compass_heading() >= 90:
        basic.show_arrow(ArrowNames.SOUTH_EAST)
    if 360 - input.compass_heading() <= 180 and 360 - input.compass_heading() >= 135:
        basic.show_arrow(ArrowNames.SOUTH)
    if 360 - input.compass_heading() <= 225 and 360 - input.compass_heading() >= 180:
        basic.show_arrow(ArrowNames.SOUTH_WEST)
    if 360 - input.compass_heading() <= 270 and 360 - input.compass_heading() >= 225:
        basic.show_arrow(ArrowNames.WEST)
    if 360 - input.compass_heading() <= 315 and 360 - input.compass_heading() >= 270:
        basic.show_arrow(ArrowNames.NORTH_WEST)
    if 360 - input.compass_heading() <= 360 and 360 - input.compass_heading() >= 315:
        basic.show_arrow(ArrowNames.NORTH)
    basic.pause(100)
    basic.clear_screen()
basic.forever(on_forever)

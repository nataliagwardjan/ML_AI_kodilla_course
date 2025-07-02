import random
from turtle import Turtle

from const import LEFT, BOTTOM, MARGIN, WIDTH, HEIGHT, TOP, RIGHT


def get_forward(forward_type: bool, width_element_length: int):
    if forward_type:
        forward = random.randint(1, width_element_length)
    else:
        forward = - random.randint(1, width_element_length)
    return forward


def get_x_condition(forward_type: bool, current_x: int, forward_value: int = 0):
    if forward_type:
        return current_x + forward_value <= RIGHT
    else:
        return current_x + forward_value >= LEFT


def draw_background(turtle: Turtle, colour: str = "#007FFF"):
    turtle.penup()
    turtle.goto(LEFT, BOTTOM)
    turtle.color(colour)
    turtle.pendown()
    turtle.begin_fill()
    for i in range(4):
        if i % 2 == 0:
            turtle.forward(WIDTH)
        else:
            turtle.forward(HEIGHT)
        turtle.left(90)
    turtle.end_fill()


def draw_sun(turtle: Turtle):
    turtle.penup()
    turtle.goto(RIGHT - 150, TOP - 100)
    turtle.color("#FFBF00")
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(radius=25)
    turtle.end_fill()


def draw_hill(turtle: Turtle,
              colour: str = "#6EBE9F",
              min_angle: int = 130,
              max_angle: int = 175,
              forward_type: bool = False,
              width_value_start: int = (WIDTH * 3) // 4
              ):
    height_value = HEIGHT // 3
    height_end_position = TOP - height_value
    width_start_position = LEFT + width_value_start

    turtle.penup()
    turtle.goto(width_start_position, BOTTOM)
    turtle.color(colour)
    turtle.pendown()
    turtle.begin_fill()

    turtle_x, turtle_y = turtle.position()
    while get_x_condition(forward_type=forward_type, current_x=turtle_x) and turtle_y <= height_end_position:
        forward = get_forward(forward_type=forward_type, width_element_length=50)
        number = 0
        while get_x_condition(forward_type=forward_type, current_x=turtle_x, forward_value=forward) and number <= 10:
            forward = get_forward(forward_type=forward_type, width_element_length=50)
            print(f"New forward = {forward}")
            number += 1

        if number == 10:
            difference = height_end_position - turtle_y
            if difference <= 20:
                turtle.goto(RIGHT if forward_type else LEFT, height_end_position)
            else:
                turtle.goto(RIGHT if forward_type else LEFT, turtle_y)
        else:
            turtle.forward(forward)
        turtle_x, turtle_y = turtle.position()
        angle = random.randint(min_angle, max_angle)
        if turtle_y >= BOTTOM:
            turtle.left(angle)
            turtle.forward(1.5 * forward if forward_type else - 0.4 * forward)
            turtle.right(angle)
        turtle_x, turtle_y = turtle.position()

    if not (turtle_x == (RIGHT if forward_type else LEFT) and turtle_y == height_end_position):
        turtle.goto(RIGHT if forward_type else LEFT, height_end_position)

    turtle.goto(RIGHT if forward_type else LEFT, BOTTOM)
    turtle.goto(width_start_position, BOTTOM)
    turtle.end_fill()


def write_sentence(turtle: Turtle,
                   position_width: int = (LEFT + MARGIN),
                   position_height: int = (BOTTOM + MARGIN),
                   pencolor: str = "black",
                   text: str = "Monty Python's Camelot!"):
    turtle.penup()
    turtle.goto(position_width, position_height)
    turtle.pendown()
    turtle.pencolor(pencolor)
    turtle.write(text, font=("Calibri", 18, "bold"))


def draw_cloud(turtle: Turtle,
               position_x: int,
               position_y: int):
    parameters = [(20, position_x, position_y),
                  (15, position_x - 25, position_y),
                  (15, position_x, position_y - 20),
                  (15, position_x + 25, position_y),
                  (15, position_x, position_y + 20),
                  (15, position_x - 15, position_y - 15),
                  (15, position_x + 15, position_y - 15),
                  (15, position_x - 15, position_y + 15),
                  (15, position_x + 15, position_y + 15)
                  ]
    turtle.color("#FFFFFF")
    for parameter in parameters:
        r, x, y = parameter
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(r)
        turtle.end_fill()





def draw_door(turtle: Turtle,
              position_x: int,
              position_y: int):
    pass


def draw_window(turtle: Turtle,
                position_x: int,
                position_y: int):
    pass


def draw_tower(turtle: Turtle,
               position_x: int,
               position_y: int,
               width: int,
               height: int):
    pass


def draw_castle(turtle: Turtle):
    x = -400
    y = 20
    colour = "#778899"
    turtle.penup()
    turtle.goto(x, y)
    turtle.color(colour)
    turtle.pendown()
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward()
    turtle.end_fill()
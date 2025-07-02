import turtle

from const import WIDTH, HEIGHT
from draw import write_sentence, draw_background, draw_hill, draw_sun, draw_cloud

turtle.setup(width=WIDTH, height=HEIGHT)
monty = turtle.Turtle()
monty.speed(7)

draw_background(turtle=monty)
draw_hill(turtle=monty,
          colour="#19A56F",
          min_angle=45,
          max_angle=70,
          forward_type=True,
          width_value_start=WIDTH // 2)
draw_hill(turtle=monty)
draw_sun(turtle=monty)
draw_cloud(turtle=monty, position_x=200,position_y=135)
draw_cloud(turtle=monty, position_x=235,position_y=150)
draw_cloud(turtle=monty, position_x=-235,position_y=160)
draw_cloud(turtle=monty, position_x=-435,position_y=225)
write_sentence(turtle=monty)

turtle.done()

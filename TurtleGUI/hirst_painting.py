import turtle as t
import colorgram
import random

tim = t.Turtle()
tim.hideturtle()
t.colormode(255)
colorgram_colors = colorgram.extract("hirst.jpg", 20)
colors = [tuple(color.rgb) for color in colorgram_colors]

tim.penup()
tim.setheading(230)
tim.forward(400)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(colors))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

# Alternative 2

# def print_dot():
#     tim.setheading(0)
#     for _ in range(10):
#         tim.dot(20, random.choice(colors))
#         tim.penup()
#         tim.fd(50)

# def change_direction():
#     tim.setheading(90)
#     tim.forward(50)




# for _ in range(10):
#     print_dot()
#     change_direction()
#     tim.setheading(180)
#     tim.forward(500)

screen = t.Screen()
screen.exitonclick()
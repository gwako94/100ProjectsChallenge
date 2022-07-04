import random
import turtle as t

tim = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b

tim.speed("fastest")

def draw_spirograph(gap):
    for _ in range(360 // gap):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + gap)

draw_spirograph(5)







screen = t.Screen()
screen.exitonclick()


# directions = [0, 90, 180, 270]
# tim.pensize(15)


# for _ in range(200):
#     tim.color(random_color())
#     tim.forward(30)
#     tim.setheading(random.choice(directions))



# Alternative 1
# num_of_sides=3
# max_num_sides = 11
# colors = ['red', 'blue', 'indigo', 'green', 'lime', 'dark slate blue', 'black', 'cyan']
# while num_of_sides < max_num_sides:
#     tim.color(colors[num_of_sides - 3])
#     for _ in range(num_of_sides):
#         angle = 360 // num_of_sides
#         tim.forward(100)
#         tim.right(angle)
#     num_of_sides+=1


# def draw_shape(num_of_sides):
#     tim.color(colors[num_of_sides-3])
#     for _ in range(num_of_sides):
#         angle = 360 // num_of_sides
#         tim.forward(100)
#         tim.right(angle)

# for num in range(3, 11):
#     draw_shape(num)

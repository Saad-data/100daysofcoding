import turtle as t
import random

tom =t.Turtle()
tom.shape("turtle")

#shades of color
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    random_color = (r, g, b)#created the tuple
    return random_color



#list of colour
#colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "Yellow", "blue", "orange", "black", "LightSeaGreen", "black", "SlateGray", "SeaGreen"]

#the line turtle ia drawing will be much thicker by using this
tom.pensize(15)

#list of direction
directions = [0, 90, 180, 270, 360]

#if we want to increase the speed
#fast
tom.speed("fastest")

for _ in range(200):
    tom.color(random_color())
    tom.forward(40)
    tom.setheading(random.choice(directions))

#shows a the screen till a click
# screen = Screen()
# screen.exitonclick()





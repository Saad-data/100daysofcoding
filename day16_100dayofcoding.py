# # import another_module
# # print(another_module.file)
#
# from turtle import Turtle, Screen
#
# #we must have to put the parntheses in the end of the blueprint
# timmy = Turtle()
#
# #we printed the new turtle object
# print(timmy)
#
# # the output will show the screen with the turtle
# timmy.shape("turtle")
#
# #changing the colour of turtle
#
# timmy.color("blue","green")
#
# #moving turtle forward
# timmy.forward(100.0)
#
# #example of the object attributres
# my_screen = Screen()
# print(my_screen.canvheight)
#
# #example of the object Methods
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

# here my_screen is the object and the exitonclick is the method --> function
#the screen appear on the screen and when you click it exit
#the size of the screen
#what WE SEE SEE HEERE is how to create the object,
#how to use the attributes by using the name of object
#how to use the method/ call them when required with object

#USING more extrenal libaries of python

from prettytable import PrettyTable

#creating the object "named" table
table = PrettyTable()
#creating the challenged table

adding_table = table.add_column("Pokemon Name", ["Pokachu", "Squirtle","Charmandar"])
adding_table = table.add_column("type", ["Electric","Water","Fire"])

#how to do the table alignment
table.align = "l"
print(table)


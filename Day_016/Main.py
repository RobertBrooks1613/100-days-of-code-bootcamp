from turtle import Turtle, Screen
import random
from prettytable import PrettyTable
table = PrettyTable()
pokemon = ["Pikachu", "Squirtle", "Charmander"]
types = ["Electric", "Water", "Fire"]
table.add_column("Pokemon Name", pokemon)
table.add_column("Type", types)
table.align = "l"
print(table)

# loop = 0
# timmy = Turtle()
# my_screen = Screen()
#
# timmy.color("DarkSeaGreen")
# timmy.shape("turtle")
# timmy.speed(1)
# while True:
#     if loop >= 20:
#         break
#     timmy.forward(random.randint(1,100))
#     timmy.left(random.randint(1,100))
#     timmy.forward(random.randint(1,100))
#
# my_screen.exitonclick()

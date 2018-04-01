# IMPORTS
from random import randint
from turtle import *
from math import sqrt
from time import sleep
import sys, os

print("Game design credit goes to Google.")

#os.system("TASKKILL /F /IM explorer.exe")

# Check if module is being imported or not
if __name__ == "__main__":
    pass    # If not being imported, do nothing
else:
    x = 0
    while True:
        if x is 0:
            print("Please do not import TicTacToe into another module.\nRun the module directly.")
            x = 1
            sleep(2)
            #os.startfile("C:\Windows\explorer.exe")
            #os.system("TASKKILL /F /IM pythonw.exe")
            #os.system("TASKKILL /F /IM python.exe")
            sys.exit()


print("Use the numbers on your numpad to play.\nClick anywhere on the screen to show help!\n")

# VARIABLES
# Set up window resolutions. You can adjust these but keep in mind the game will look somewhat disproportionated.
screenResX = 500
screenResY = 500

# Fixed resolution for grid
x_adjusted = screenResX / 3 / 2
y_adjusted = screenResY / 3 / 2

# set up grid center coordinates // Grid x => x = number on the numpad
grid1 = (-x_adjusted * 2, -y_adjusted * 2)
grid2 = (-x_adjusted * 0, -y_adjusted * 2)
grid3 = (x_adjusted * 2, -y_adjusted * 2)
grid4 = (-x_adjusted * 2, y_adjusted * 0)
grid5 = (-x_adjusted * 0, y_adjusted * 0)
grid6 = (x_adjusted * 2, y_adjusted * 0)
grid7 = (-x_adjusted * 2, y_adjusted * 2)
grid8 = (-x_adjusted * 0, y_adjusted * 2)
grid9 = (x_adjusted * 2, y_adjusted * 2)


# Choosing starting player: 0 => circle; 1 => cross
def choosestartingplayer():
    global startingPlayer
    startingPlayer = randint(0, 1)
    if startingPlayer == 0:
        print("Starting Player is circle!")
    else:
        print("Starting Player is cross!")
choosestartingplayer()


# variables used at the end of the game
global ready_to_end
ready_to_end = False

# GRID CHECK FOR BOTH PLAYERS
global numpad1_check
numpad1_check = False
global numpad2_check
numpad2_check = False
global numpad3_check
numpad3_check = False
global numpad4_check
numpad4_check = False
global numpad5_check
numpad5_check = False
global numpad6_check
numpad6_check = False
global numpad7_check
numpad7_check = False
global numpad8_check
numpad8_check = False
global numpad9_check
numpad9_check = False

# GRID CHECK FOR CIRCLE
global numpad1_check_circle
numpad1_check_circle = False
global numpad2_check_circle
numpad2_check_circle = False
global numpad3_check_circle
numpad3_check_circle = False
global numpad4_check_circle
numpad4_check_circle = False
global numpad5_check_circle
numpad5_check_circle = False
global numpad6_check_circle
numpad6_check_circle = False
global numpad7_check_circle
numpad7_check_circle = False
global numpad8_check_circle
numpad8_check_circle = False
global numpad9_check_circle
numpad9_check_circle = False

# GRID CHECK FOR CROSS
global numpad1_check_cross
numpad1_check_cross = False
global numpad2_check_cross
numpad2_check_cross = False
global numpad3_check_cross
numpad3_check_cross = False
global numpad4_check_cross
numpad4_check_cross = False
global numpad5_check_cross
numpad5_check_cross = False
global numpad6_check_cross
numpad6_check_cross = False
global numpad7_check_cross
numpad7_check_cross = False
global numpad8_check_cross
numpad8_check_cross = False
global numpad9_check_cross
numpad9_check_cross = False

# SETUP
# Set up screen
setup(screenResX, screenResY)
title('TicTacToe')
colormode(255)
bgcolor(20, 189, 172)
tracer(0, 0)

# Turtle(s)
draw = Turtle()
draw.hideturtle()
drawmenu = Turtle()
drawmenu.hideturtle()


def draw_grid():
    draw.pensize((screenResX + screenResY) / 2 * 10 / 500)
    draw.speed('fastest')
    draw.hideturtle()
    draw.color(16, 170, 155)
    draw.penup()  # START DRAWING
    draw.setpos(x_adjusted, y_adjusted * 3)
    draw.pendown()
    draw.setpos(x_adjusted, -y_adjusted * 3)
    draw.penup()
    draw.setpos(-x_adjusted, y_adjusted * 3)
    draw.pendown()
    draw.setpos(-x_adjusted, -y_adjusted * 3)
    draw.penup()
    draw.setpos(-x_adjusted * 3, y_adjusted)
    draw.pendown()
    draw.setpos(x_adjusted * 3, y_adjusted)
    draw.penup()
    draw.setpos(-x_adjusted * 3, -y_adjusted)
    draw.pendown()
    draw.setpos(x_adjusted * 3, -y_adjusted)
    draw.penup()
    draw.color("blue")


# Draw cross
def cross(grid):
    cross_length = sqrt((x_adjusted / 2) ** 2 + (y_adjusted / 2) ** 2)

    draw.color(84, 84, 84)
    draw.pensize((screenResX + screenResY) / 2 * 10 / 500)
    draw.setpos(grid)
    draw.pendown()
    draw.left(45)
    draw.forward(cross_length)
    draw.backward(cross_length * 2)
    draw.forward(cross_length)
    draw.right(90)
    draw.forward(cross_length)
    draw.backward(cross_length * 2)
    draw.forward(cross_length)
    draw.left(45)
    draw.penup()


# Draw circle
def circle(grid):
    circle_radius = (x_adjusted + y_adjusted) / 2 * 1 / 2 + 5  # +5 to make cross and circle about the same size

    draw.color(242, 235, 211)
    draw.pensize((screenResX + screenResY) / 2 * 10 / 500)
    draw.setpos(grid)
    draw.right(90)
    draw.forward(circle_radius)
    draw.left(90)
    draw.pendown()
    draw.circle(circle_radius)
    draw.penup()


draw_grid()


def solutioncheck():
    circle_color = (242, 235, 211)  # Credit goes to Google for theme color
    cross_color = (84, 84, 84)
    global numpad1_check_circle  # Import variables into function
    global numpad1_check_cross
    global numpad2_check_circle
    global numpad2_check_cross
    global numpad3_check_circle
    global numpad3_check_cross
    global numpad4_check_circle
    global numpad4_check_cross
    global numpad5_check_circle
    global numpad5_check_cross
    global numpad6_check_circle
    global numpad6_check_cross
    global numpad7_check_circle
    global numpad7_check_cross
    global numpad8_check_circle
    global numpad8_check_cross
    global numpad9_check_circle
    global numpad9_check_cross
    ######################################################
    if numpad7_check_circle is True and numpad8_check_circle is True and numpad9_check_circle is True:  # 789 circle
        end(circle, circle_color, -x_adjusted * 3, y_adjusted * 2, x_adjusted * 3, y_adjusted * 2)
    elif numpad4_check_circle is True and numpad5_check_circle is True and numpad6_check_circle is True:  # 456 circle
        end(circle, circle_color, -x_adjusted * 3, y_adjusted * 0, x_adjusted * 3, y_adjusted * 0)
    elif numpad1_check_circle is True and numpad2_check_circle is True and numpad3_check_circle is True:  # 123 circle
        end(circle, circle_color, -x_adjusted * 3, -y_adjusted * 2, x_adjusted * 3, -y_adjusted * 2)
    elif numpad7_check_circle is True and numpad4_check_circle is True and numpad1_check_circle is True:  # 741 circle
        end(circle, circle_color, -x_adjusted * 2, y_adjusted * 3, -x_adjusted * 2, -y_adjusted * 3)
    elif numpad8_check_circle is True and numpad5_check_circle is True and numpad2_check_circle is True:  # 852 circle
        end(circle, circle_color, x_adjusted * 0, y_adjusted * 3, x_adjusted * 0, -y_adjusted * 3)
    elif numpad9_check_circle is True and numpad6_check_circle is True and numpad3_check_circle is True:  # 963 circle
        end(circle, circle_color, x_adjusted * 2, y_adjusted * 3, x_adjusted * 2, -y_adjusted * 3)
    elif numpad9_check_circle is True and numpad5_check_circle is True and numpad1_check_circle is True:  # 951 circle
        end(circle, circle_color, x_adjusted * 3, y_adjusted * 3, -x_adjusted * 3, -y_adjusted * 3)
    elif numpad7_check_circle is True and numpad5_check_circle is True and numpad3_check_circle is True:  # 753 circle
        end(circle, circle_color, -x_adjusted * 3, y_adjusted * 3, x_adjusted * 3, -y_adjusted * 3)
    ####################################################################################################################
    elif numpad7_check_cross is True and numpad8_check_cross is True and numpad9_check_cross is True:  # 789 cross
        end(cross, cross_color, -x_adjusted * 3, y_adjusted * 2, x_adjusted * 3, y_adjusted * 2)
    elif numpad4_check_cross is True and numpad5_check_cross is True and numpad6_check_cross is True:  # 456 cross
        end(cross, cross_color, -x_adjusted * 3, y_adjusted * 0, x_adjusted * 3, y_adjusted * 0)
    elif numpad1_check_cross is True and numpad2_check_cross is True and numpad3_check_cross is True:  # 123 cross
        end(cross, cross_color, -x_adjusted * 3, -y_adjusted * 2, x_adjusted * 3, -y_adjusted * 2)
    elif numpad7_check_cross is True and numpad4_check_cross is True and numpad1_check_cross is True:  # 741 cross
        end(cross, cross_color, -x_adjusted * 2, y_adjusted * 3, -x_adjusted * 2, -y_adjusted * 3)
    elif numpad8_check_cross is True and numpad5_check_cross is True and numpad2_check_cross is True:  # 852 cross
        end(cross, cross_color, x_adjusted * 0, y_adjusted * 3, x_adjusted * 0, -y_adjusted * 3)
    elif numpad9_check_cross is True and numpad6_check_cross is True and numpad3_check_cross is True:  # 963 cross
        end(cross, cross_color, x_adjusted * 2, y_adjusted * 3, x_adjusted * 2, -y_adjusted * 3)
    elif numpad9_check_cross is True and numpad5_check_cross is True and numpad1_check_cross is True:  # 951 cross
        end(cross, cross_color, x_adjusted * 3, y_adjusted * 3, -x_adjusted * 3, -y_adjusted * 3)
    elif numpad7_check_cross is True and numpad5_check_cross is True and numpad3_check_cross is True:  # 753 cross
        end(cross, cross_color, -x_adjusted * 3, y_adjusted * 3, x_adjusted * 3, -y_adjusted * 3)
    else:
        if numpad1_check == True and numpad2_check == True and numpad3_check == True and numpad4_check == True and numpad5_check == True and numpad6_check == True and numpad7_check == True and numpad8_check == True and numpad9_check == True:
            end(0, 0, 0, 0, 0, 0)


def end(player, color, x_start, y_start, x_end, y_end):
    global ready_to_end
    global numpad1_check
    numpad1_check = True
    global numpad2_check
    numpad2_check = True
    global numpad3_check
    numpad3_check = True
    global numpad4_check
    numpad4_check = True
    global numpad5_check
    numpad5_check = True
    global numpad6_check
    numpad6_check = True
    global numpad7_check
    numpad7_check = True
    global numpad8_check
    numpad8_check = True
    global numpad9_check
    numpad9_check = True
    # Write winning text, etc...
    if player == circle:
        draw.up()
        draw.setpos(x_start, y_start)
        draw.color(color)
        draw.down()
        draw.setpos(x_end, y_end)
        draw.up()
        draw.color(0, 0, 0)
        draw.setpos(x_adjusted * 0, y_adjusted * 1 - 15)
        draw.write("Circle won the game!", move=False, align="center", font=("Arial", 25, "bold", "italic"))
        draw.setpos(x_adjusted * 0, -y_adjusted * 1 - 15)
        draw.write("Circle won the game!", move=False, align="center", font=("Arial", 25, "bold", "italic"))
    elif player == cross:
        draw.up()
        draw.setpos(x_start, y_start)
        draw.color(color)
        draw.down()
        draw.setpos(x_end, y_end)
        draw.up()
        draw.color(255, 255, 255)
        draw.setpos(x_adjusted * 0, y_adjusted * 1 - 15)
        draw.write("Cross won the game!", move=False, align="center", font=("Arial", 25, "bold", "italic"))
        draw.setpos(x_adjusted * 0, -y_adjusted * 1 - 15)
        draw.write("Cross won the game!", move=False, align="center", font=("Arial", 25, "bold", "italic"))
    else:
        draw.color(127, 127, 127)
        draw.setpos(x_adjusted * 0, y_adjusted * 1 - 15)
        draw.write("Draw!", move=False, align="center", font=("Arial", 25, "bold", "italic"))
        draw.setpos(x_adjusted * 0, -y_adjusted * 1 - 15)
        draw.write("Draw!", move=False, align="center", font=("Arial", 25, "bold", "italic"))
    sleep(1)  # wait x seconds
    draw.undo()
    draw.undo()
    draw.undo()  # remove winning text
    draw.color(0, 29, 255)
    draw.setpos(x_adjusted * 0, y_adjusted * 1 - 15)
    draw.write("Press 0 to exit, or 1 to restart !", move=False, align="center", font=("Arial", 25, "bold", "italic"))
    draw.setpos(x_adjusted * 0, -y_adjusted * 1 - 15)
    draw.write("Press 0 to exit, or 1 to restart !", move=False, align="center", font=("Arial", 25, "bold", "italic"))
    ready_to_end = True


def numpad0():
    global ready_to_end
    if ready_to_end:
        print("Shutting Down...\n")
        #os.startfile("C:\Windows\explorer.exe")
        os.system("TASKKILL /F /IM pythonw.exe")
        os.system("TASKKILL /F /IM python.exe")
        sys.exit()
    else:
        pass


def numpad1():
    global ready_to_end
    global numpad1_check_circle
    global numpad1_check_cross
    global numpad1_check
    global numpad2_check_circle
    global numpad2_check_cross
    global numpad2_check
    global numpad3_check_circle
    global numpad3_check_cross
    global numpad3_check
    global numpad4_check_circle
    global numpad4_check_cross
    global numpad4_check
    global numpad5_check_circle
    global numpad5_check_cross
    global numpad5_check
    global numpad6_check_circle
    global numpad6_check_cross
    global numpad6_check
    global numpad7_check_circle
    global numpad7_check_cross
    global numpad7_check
    global numpad8_check_circle
    global numpad8_check_cross
    global numpad8_check
    global numpad9_check_circle
    global numpad9_check_cross
    global numpad9_check
    global startingPlayer
    if not numpad1_check:
        if startingPlayer == 0:
            circle(grid1)
            startingPlayer = 1
            numpad1_check_circle = True
            print("Grid1 has been filled with a circle!")
        else:
            cross(grid1)
            startingPlayer = 0
            numpad1_check_cross = True
            print("Grid1 has been filled with a cross!")
        numpad1_check = True
        solutioncheck()
    elif ready_to_end:
        print("restarting...\n")
        draw.reset()
        draw_grid()
        ready_to_end = False
        numpad1_check_circle = False
        numpad1_check_cross = False
        numpad1_check = False
        numpad2_check_circle = False
        numpad2_check_cross = False
        numpad2_check = False
        numpad3_check_circle = False
        numpad3_check_cross = False
        numpad3_check = False
        numpad4_check_circle = False
        numpad4_check_cross = False
        numpad4_check = False
        numpad5_check_circle = False
        numpad5_check_cross = False
        numpad5_check = False
        numpad6_check_circle = False
        numpad6_check_cross = False
        numpad6_check = False
        numpad7_check_circle = False
        numpad7_check_cross = False
        numpad7_check = False
        numpad8_check_circle = False
        numpad8_check_cross = False
        numpad8_check = False
        numpad9_check_circle = False
        numpad9_check_cross = False
        numpad9_check = False
        choosestartingplayer()  # Choose new startingPlayer


def numpad2():
    global numpad2_check_circle
    global numpad2_check_cross
    global numpad2_check
    global startingPlayer
    if not numpad2_check:
        if startingPlayer == 0:
            circle(grid2)
            startingPlayer = 1
            numpad2_check_circle = True
            print("Grid2 has been filled with a circle!")
        else:
            cross(grid2)
            startingPlayer = 0
            numpad2_check_cross = True
            print("Grid2 has been filled with a cross!")
        numpad2_check = True
        solutioncheck()


def numpad3():
    global numpad3_check_circle
    global numpad3_check_cross
    global numpad3_check
    global startingPlayer
    if not numpad3_check:
        if startingPlayer == 0:
            circle(grid3)
            startingPlayer = 1
            numpad3_check_circle = True
            print("Grid3 has been filled with a circle!")
        else:
            cross(grid3)
            startingPlayer = 0
            numpad3_check_cross = True
            print("Grid3 has been filled with a cross!")
        numpad3_check = True
        solutioncheck()


def numpad4():
    global numpad4_check_circle
    global numpad4_check_cross
    global numpad4_check
    global startingPlayer
    if not numpad4_check:
        if startingPlayer == 0:
            circle(grid4)
            startingPlayer = 1
            numpad4_check_circle = True
            print("Grid4 has been filled with a circle!")
        else:
            cross(grid4)
            startingPlayer = 0
            numpad4_check_cross = True
            print("Grid4 has been filled with a cross!")
        numpad4_check = True
        solutioncheck()


def numpad5():
    global numpad5_check_circle
    global numpad5_check_cross
    global numpad5_check
    global startingPlayer
    if not numpad5_check:
        if startingPlayer == 0:
            circle(grid5)
            startingPlayer = 1
            numpad5_check_circle = True
            print("Grid5 has been filled with a circle!")
        else:
            cross(grid5)
            startingPlayer = 0
            numpad5_check_cross = True
            print("Grid5 has been filled with a cross!")
        numpad5_check = True
        solutioncheck()


def numpad6():
    global numpad6_check_circle
    global numpad6_check_cross
    global numpad6_check
    global startingPlayer
    if not numpad6_check:
        if startingPlayer == 0:
            circle(grid6)
            startingPlayer = 1
            numpad6_check_circle = True
            print("Grid6 has been filled with a circle!")
        else:
            cross(grid6)
            startingPlayer = 0
            numpad6_check_cross = True
            print("Grid6 has been filled with a cross!")
        numpad6_check = True
        solutioncheck()


def numpad7():
    global numpad7_check_circle
    global numpad7_check_cross
    global numpad7_check
    global startingPlayer
    if not numpad7_check:
        if startingPlayer == 0:
            circle(grid7)
            startingPlayer = 1
            numpad7_check_circle = True
            print("Grid7 has been filled with a circle!")
        else:
            cross(grid7)
            startingPlayer = 0
            numpad7_check_cross = True
            print("Grid7 has been filled with a cross!")
        numpad7_check = True
        solutioncheck()


def numpad8():
    global numpad8_check_circle
    global numpad8_check_cross
    global numpad8_check
    global startingPlayer
    if not numpad8_check:
        if startingPlayer == 0:
            circle(grid8)
            startingPlayer = 1
            numpad8_check_circle = True
            print("Grid8 has been filled with a circle!")
        else:
            cross(grid8)
            startingPlayer = 0
            numpad8_check_cross = True
            print("Grid8 has been filled with a cross!")
        numpad8_check = True
        solutioncheck()


def numpad9():
    global numpad9_check_circle
    global numpad9_check_cross
    global numpad9_check
    global startingPlayer
    if not numpad9_check:
        if startingPlayer == 0:
            circle(grid9)
            startingPlayer = 1
            numpad9_check_circle = True
            print("Grid9 has been filled with a circle!")
        else:
            cross(grid9)
            startingPlayer = 0
            numpad9_check_cross = True
            print("Grid9 has been filled with a cross!")
        numpad9_check = True
        solutioncheck()


def click(x, y):    # Kinda useless...
    if ready_to_end:
        pass
    else:
        draw.color(255, 255, 255)
        draw.setpos(-x_adjusted * 2, -y_adjusted * 2)
        draw.write("1", move=False, align="center", font=("Arial", 25, "bold", "italic"))
        draw.setpos(-x_adjusted * 0, -y_adjusted * 2)
        draw.write("2", move=False, align="center", font=("Arial", 25, "bold", "italic"))
        draw.setpos(x_adjusted * 2, -y_adjusted * 2)
        draw.write("3", move=False, align="center", font=("Arial", 25, "bold", "italic"))
        draw.setpos(-x_adjusted * 2, -y_adjusted * 0)
        draw.write("4", move=False, align="center", font=("Arial", 25, "bold", "italic"))
        draw.setpos(-x_adjusted * 0, -y_adjusted * 0)
        draw.write("5", move=False, align="center", font=("Arial", 25, "bold", "italic"))
        draw.setpos(x_adjusted * 2, -y_adjusted * 0)
        draw.write("6", move=False, align="center", font=("Arial", 25, "bold", "italic"))
        draw.setpos(-x_adjusted * 2, y_adjusted * 2)
        draw.write("7", move=False, align="center", font=("Arial", 25, "bold", "italic"))
        draw.setpos(-x_adjusted * 0, y_adjusted * 2)
        draw.write("8", move=False, align="center", font=("Arial", 25, "bold", "italic"))
        draw.setpos(x_adjusted * 2, y_adjusted * 2)
        draw.write("9", move=False, align="center", font=("Arial", 25, "bold", "italic"))
        sleep(0.5)
        draw.undo()
        draw.undo()
        draw.undo()
        draw.undo()
        draw.undo()
        draw.undo()
        draw.undo()
        draw.undo()
        draw.undo()
        draw.undo()
        draw.undo()
        draw.undo()
        draw.undo()
        draw.undo()
        draw.undo()
        draw.undo()
        draw.undo()
        '''clickpos = (x, y)
        print(clickpos)'''


onkey(numpad0, "0")
onkey(numpad1, "1")
onkey(numpad2, "2")
onkey(numpad3, "3")
onkey(numpad4, "4")
onkey(numpad5, "5")
onkey(numpad6, "6")
onkey(numpad7, "7")
onkey(numpad8, "8")
onkey(numpad9, "9")
onscreenclick(click)
listen()
mainloop()  # Avoid screen refreshes

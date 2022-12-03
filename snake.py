from turtle import *
from gamebase import square
from random import randrange


snake = [[0,0],[10,0],[20,0],[30,0],[40,0],[50,0]]
apple_x=randrange(-200,200, 10)
apple_y=randrange(-200,200, 10)
aim_x=10
aim_y=0

def change(x,y):
    global aim_x,aim_y
    aim_x=x
    aim_y=y

def inside_snake():
    for n in range(len(snake)-1):
        if snake[-1][0] == snake [n][0] and snake[-1][1] == snake[n][1]:
            return True
    return False

def inside():
    if -210<-snake[-1][0]<= 200 and -210<=snake[-1][1]<=200:
        return True
    else :
        return False


def gameLoop():
    global apple_x,apple_y 
    
    snake.append([snake[-1][0]+aim_x, snake[-1][1]+aim_y])
    if (not inside()) or inside_snake():
        return
    if snake[-1][0]!=apple_x or snake[-1][1]!=apple_y:
        snake.pop(0)
    else :
        apple_x=randrange(-200,200, 10)
        apple_y=randrange(-200,200, 10)
    clear()
    square(-210,-200,410,"black")
    square(apple_x,apple_y,10,"red")
    for n in range(len(snake)):
        square(snake[n][0],snake[n][1],10,"black")


    

    ontimer(gameLoop,150)
    update()

setup(420,420,0,0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(0,10),"w")
onkey(lambda: change(0,-10),"s")
onkey(lambda: change(-10,0),"a")
onkey(lambda: change(10,0),"d")
gameLoop()
done()
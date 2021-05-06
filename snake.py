from turtle import *
from random import randrange
from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, snake_color)

    square(food.x, food.y, 9, food_color)
    update()
    ontimer(move, 100)


def coloringfood():
    
    randcfood=randrange(0,5)
    
    if(randcfood==0):
        return 'BLUE'
    
    elif(randcfood==1):
        return 'PINK'
    
    elif(randcfood==2):
        return 'YELLOW'
    
    elif(randcfood==3):
        return 'GREEN'
    
    elif(randcfood==4):
        return 'TEAL'     


def coloringsnake():
    
    randcsnake=randrange(0,5)
    
    if(randcsnake==0):
        return 'ORANGE'
    
    elif(randcsnake==1):
        return 'GREEN4'
    
    elif(randcsnake==2):
        return 'BLACK'
    
    elif(randcsnake==3):
        return 'CYAN'
    
    elif(randcfood==4):
         return 'MAGENTA'


food_color = coloringfood()       
snake_color = coloringsnake()


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()

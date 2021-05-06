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
        # Crea la variable que indica si la comida ya cambio de posición
        food_changed = False
        # Mientras no haya cambiado la comida, sigue intentando
        while not food_changed:
            food_changed = True # Supone que la comida cambia de posición
            dir = randrange(0, 4) # Genera un número aleatorio entre 0 y 4
            if dir == 0 and inside(food + vector(10, 0)):
                # Movimiento a la derecha
                food.move(vector(10, 0))
            elif dir == 1 and inside(food + vector(0, 10)):
                # Movimiento hacia arriba
                food.move(vector(0, 10))
            elif dir == 2 and inside(food + vector(-10, 0)):
                # Movimiento a la izquierda
                food.move(vector(-10, 0))
            elif dir == 3 and inside(food + vector(0, -10)):
                # Movimiento habia abajo
                food.move(vector(0, -10))
            else: 
                # El movimiento no fue válido
                food_changed = False # No se ha movido la comida

    clear()

    for body in snake:
        # Escoge la posición y el color de la serpiente y la comida
        square(body.x, body.y, 9, snake_color) 

    square(food.x, food.y, 9, food_color)
    update()
    ontimer(move, 100)


def coloring_food():
    """
Cambia el color de la comida en cada corrida aleatoriamente 
"""
    
    randcfood=randrange(0,5)# Escoge un valor entre 0 y 4
  # Escoge un color diferente dependiendo del número  
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


def coloring_snake():
    """
Cambia el color de la serpiente en cada corrida aleatoriamente 
"""
    
    randcsnake=randrange(0,5)# Escoge un valor entre 0 y 4 
    # Escoge un color diferente dependiendo del número 
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

# Guarda el color aleatorio de la comida  
food_color = coloring_food()
# Guarda el color aleatorio de la serpiente
snake_color = coloring_snake()


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

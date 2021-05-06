# Código modificado
# David Damián Galán
# Angélica Sofía Ramírez Porras

from turtle import * # Importa todas las funciones de turtle
from random import randrange # Importa randrange de random
# Importa funciones vector y square de freegames
from freegames import square, vector 
food = vector(0, 0) # posición inicial de comida 
snake = [vector(10, 0)] # posición inicial de snake
aim = vector(0, -10) # vector de movimiento


def change(x, y):
    """
    Cambia la dirección de la snake
    x = coordenada x
    y = coordenada y 
    """ 
    aim.x = x
    aim.y = y

    
def inside(head):
    """ 
    Para que la coordenada head esté adentro del recuadro 
    head = coordenada evaluada
    """
    return -200 < head.x < 190 and -200 < head.y < 190


def move():
    """ 
    Mover la snake y la comida 
    """
    head = snake[-1].copy() # Copia la coordenada de la cabeza 
    head.move(aim) # Mueve la cabeza

    if not inside(head) or head in snake:
        # En caso de que la snake choque con el muro o sí misma, pierde 
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head) # Agrega nueva cabeza a snake

    if head == food:
        # En caso de que sí coma la snake, crece
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        # En caso de que no coma la snake, se queda igual 
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

    clear() # Borrar las figuras 

    for body in snake:
        # Dibuja la posición de snake y su color
        square(body.x, body.y, 9, snake_color) 
        
    # Coloca la comida y su color 
    square(food.x, food.y, 9, food_color)
    update() # Actualiza el dibujo 
    ontimer(move, 100) # Mover la snake cada 100 mili segundos


def coloring_food():
    """
    
    Cambia el color de la comida en cada corrida aleatoriamente

    """
    
    randcfood=randrange(0, 5) # Escoge un valor entre 0 y 4
    
    # Escoge un color diferente dependiendo del número 

    if(randcfood == 0):
        return 'BLUE'
    
    elif(randcfood == 1):
        return 'PINK'
    
    elif(randcfood == 2):
        return 'YELLOW'
    
    elif(randcfood == 3):
        return 'GREEN'
    
    elif(randcfood == 4):
        return 'TEAL'     


def coloring_snake():
    """
    
    Cambia el color de la serpiente en cada corrida aleatoriamente
    
    """
    
    randcsnake=randrange(0, 5)# Escoge un valor entre 0 y 4 
    
    # Escoge un color diferente dependiendo del número 
    
    if(randcsnake == 0):
        return 'ORANGE'
    
    elif(randcsnake == 1):
        return 'GREEN4'
    
    elif(randcsnake == 2):
        return 'BLACK'
    
    elif(randcsnake == 3):
        return 'CYAN'
    
    elif(randcsnake == 4):
         return 'MAGENTA'

        
# Guarda el color aleatorio de la comida 

food_color = coloring_food()

# Guarda el color aleatorio de la serpiente

snake_color = coloring_snake()

setup(420, 420, 370, 0) # Dimensiones del recuadro
hideturtle() # Esconde la flecha 
tracer(False) # Esconde animación de square
listen() # Captura los eventos del teclado

# Los controles del juego en el teclado 

onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')

# Inicia el juego
move()

done()

import tkinter as tk
import random

# Inicializar la ventana principal
root = tk.Tk()
root.title("Snake Game")

# Configurar el lienzo
canvas = tk.Canvas(root, width=400, height=400, bg='black')
canvas.pack()

# Inicializar la serpiente y la comida
snake = [(100, 100), (90, 100), (80, 100)]
snake_direction = 'Right'
food = None
score = 0
speed = 100

# Mostrar la puntuación
score_label = tk.Label(root, text=f"Score: {score}", font=("Helvetica", 14))
score_label.pack()

# Crear la comida en una posición aleatoria
def place_food():
    global food
    while True:
        food_x = random.randint(0, 39) * 10
        food_y = random.randint(0, 39) * 10
        food = (food_x, food_y)
        if food not in snake:
            break
    canvas.create_rectangle(food_x, food_y, food_x + 10, food_y + 10, fill='red', tag='food')

# Crear la serpiente y la comida en el lienzo
def create_objects():
    canvas.delete('snake')
    for x, y in snake:
        canvas.create_rectangle(x, y, x + 10, y + 10, fill='green', tag='snake')
    canvas.create_rectangle(food[0], food[1], food[0] + 10, food[1] + 10, fill='red', tag='food')

# Cambiar la dirección de la serpiente
def change_direction(event):
    global snake_direction
    new_direction = event.keysym
    all_directions = {'Up', 'Down', 'Left', 'Right'}
    opposites = ({'Up', 'Down'}, {'Left', 'Right'})
    if new_direction in all_directions and {new_direction, snake_direction} not in opposites:
        snake_direction = new_direction

# Mover la serpiente
def move_snake():
    global snake, food, score, speed
    head_x, head_y = snake[0]
    if snake_direction == 'Up':
        new_head = (head_x, head_y - 10)
    elif snake_direction == 'Down':
        new_head = (head_x, head_y + 10)
    elif snake_direction == 'Left':
        new_head = (head_x - 10, head_y)
    elif snake_direction == 'Right':
        new_head = (head_x + 10, head_y)
    
    snake = [new_head] + snake[:-1]
    
    if snake[0] == food:
        snake.append(snake[-1])
        canvas.delete('food')
        place_food()
        score += 10
        score_label.config(text=f"Score: {score}")
        speed = max(10, speed - 5)  # Aumentar la velocidad
    
    if check_collision():
        canvas.create_text(200, 200, text="Game Over", fill="red", font=("Helvetica", 24))
    else:
        create_objects()
        root.after(speed, move_snake)

# Verificar colisiones
def check_collision():
    head_x, head_y = snake[0]
    return (
        head_x < 0 or head_x >= 400 or head_y < 0 or head_y >= 400 or
        (head_x, head_y) in snake[1:]
    )

# Configuración inicial del juego
place_food()
create_objects()
root.bind('<KeyPress>', change_direction)
move_snake()

# Ejecutar el bucle principal de Tkinter
root.mainloop()

import gymnasium as gym
import keyboard
import matplotlib.pyplot as plt

# Crear el entorno con el modo de renderizado "rgb_array"
env = gym.make("ALE/MsPacman-v5", render_mode="rgb_array")

obs, info = env.reset()

done = False

# Diccionario para mapear las teclas a las acciones del juego
action_mapping = {
    'up': 1,     # Mover hacia arriba
    'down': 4,   # Mover hacia abajo
    'left': 3,   # Mover hacia la izquierda
    'right': 2   # Mover hacia la derecha
}

# Configurar la ventana de matplotlib
plt.ion()  # Habilitar modo interactivo
fig, ax = plt.subplots()
img = ax.imshow(env.render())  # Inicializar con la primera imagen

while not done:
    action = None

    # Captura la entrada del teclado
    if keyboard.is_pressed('up'):
        action = action_mapping['up']
    elif keyboard.is_pressed('down'):
        action = action_mapping['down']
    elif keyboard.is_pressed('left'):
        action = action_mapping['left']
    elif keyboard.is_pressed('right'):
        action = action_mapping['right']
    elif keyboard.is_pressed('esc'):
        done = True
    else: 
        action = 0

    # Si se presionó alguna tecla válida, ejecutar la acción
    if action is not None:
        obs, reward, done, truncated, info = env.step(action)

    # Renderizar el entorno capturando el frame
    frame = env.render()

    print(f"Reward: {reward}, Done: {done}, Truncated: {truncated}")
    print(f"Info: {info}")

    # Actualizar la imagen en la ventana de matplotlib
    img.set_data(frame)
    plt.draw()
    plt.pause(0.001)  # Pausar brevemente para permitir la actualización de la ventana

env.close()
plt.ioff()  # Deshabilitar modo interactivo
plt.show()

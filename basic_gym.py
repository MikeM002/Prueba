import gymnasium as gym

# Crear el entorno con el modo de renderizado "human"
env = gym.make("ALE/MsPacman-v5", render_mode="human")

obs, info = env.reset()

max_steps = 1000
steps = 0
done = False

while not done and steps < max_steps:

    # Seleccionar una acción aleatoria
    action = env.action_space.sample()

    # Ejecutar la acción en el entorno
    obs, reward, done, truncated, info = env.step(action)

    print(f"Reward: {reward}, Done: {done}, Truncated: {truncated}")
    print(f"Info: {info}")
    print(type(obs), obs.shape)

    steps += 1

env.close()
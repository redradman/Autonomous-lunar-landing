import gymnasium as gym
from stable_baselines3 import PPO
from stable_baselines3.common.env_util import make_vec_env
from stable_baselines3.common.evaluation import evaluate_policy
from stable_baselines3.common.monitor import Monitor


env = gym.make("LunarLander-v2", render_mode="human")

env.reset()
print("_____OBSERVATION SPACE_____ \n")
print("Observation Space Shape", env.observation_space.shape)
print("Sample observation", env.observation_space.sample())  # Get a random observation

print("\n _____ACTION SPACE_____ \n")
print("Action Space Shape", env.action_space.n)
print("Action Space Sample", env.action_space.sample())  # Take a random action


model = PPO("MlpPolicy", env, verbose=1)
model.learn(total_timesteps=10000)

model.save("ppo_lunar_lander")

eval_env = Monitor(gym.make("LunarLander-v2"))
mean_reward, std_reward = evaluate_policy(model, eval_env, n_eval_episodes=1000, deterministic=True)
print(f"mean_reward={mean_reward:.2f} +/- {std_reward}")

# import gym
# env = gym.make("LunarLander-v2", render_mode="human")
# observation, info = env.reset(seed=42)
# for _ in range(1000):
#    action = policy(observation)  # User-defined policy function
#    observation, reward, terminated, truncated, info = env.step(action)

#    if terminated or truncated:
#       observation, info = env.reset()
# env.close()
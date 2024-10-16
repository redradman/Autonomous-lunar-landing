import gymnasium as gym
from stable_baselines3 import DQN
from stable_baselines3.common.evaluation import evaluate_policy

env = gym.make("LunarLander-v2")

model = DQN("MlpPolicy", env, verbose=1)
model.learn(total_timesteps=10000)

# Evaluate the trained mode
mean_reward, std_reward = evaluate_policy(model, env, n_eval_episodes=10)
print(f"Mean reward: {mean_reward} +/- {std_reward}")

# Optionally, save the model
model.save("dqn_lunar_lander")


import time
# Load the model if needed
# model = DQN.load("dqn_lunar_lander")
# Visualize the model's performanceepisodes = 5
episodes = 10
done = False
for episode in range(1, episodes + 1):    
	obs = env.reset()    
    done = False    
    score = 0    
    while not done:        
    	env.render()        
        action, _states = model.predict(obs)        
        obs, reward, done, info = env.step(action)        
        score += reward    
    print(f"Episode: {episode}, Score: {score}")    
	time.sleep(1)
env.close()
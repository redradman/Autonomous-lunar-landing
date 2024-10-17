# import env
import gymnasium as gym
# import torch for NN models
import torch
import torch.nn as nn
import torch.optim as optim

# import for replay buffer
import random
from collections import deque

import numpy as np # for numerical Ops
from gymnasium.wrappers import RecordEpisodeStatistics, RecordVideo # import wrappers for recording the episode statistics and metadata when recording

np.random.seed(8) # set the seed for reproducibility

################################################################################
################################ KEY COMPONENTS ################################
################################################################################

# NETWORK architecture
class QNetwork(nn.Module):
    def __init__(self, state_dim, action_dim):
        super(QNetwork, self).__init__()
        self.fc1 = nn.Linear(state_dim, 64)
        self.fc2 = nn.Linear(64, 64)
        self.fc3 = nn.Linear(64, action_dim)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        x = self.fc3(x)
        return x

# MAKE THE REPLAY BUFFER
class ReplayBuffer:
    def __init__(self, capacity):
        self.buffer = deque(maxlen=capacity)

    def push(self, state, action, reward, next_state, done):
        self.buffer.append((state, action, reward, next_state, done))

    def sample(self, batch_size):
        return random.sample(self.buffer, batch_size)

    def size(self):
        return len(self.buffer)


# MAKE THE TRAIN FUNCTION
def train_q_network(q_network, target_network, batch, gamma, optimizer):
    states, actions, rewards, next_states, dones = zip(*batch)

    states = torch.FloatTensor(np.array(states)) # convert to np.array first to increase the computational speed
    actions = torch.LongTensor(np.array(actions))
    rewards = torch.FloatTensor(np.array(rewards))
    next_states = torch.FloatTensor(np.array(next_states))
    dones = torch.FloatTensor(np.array(dones))

    q_values = q_network(states).gather(1, actions.unsqueeze(1)).squeeze(1)
    next_q_values = target_network(next_states).max(1)[0]
    expected_q_values = rewards + gamma * next_q_values * (1 - dones)

    loss = (q_values - expected_q_values.detach()).pow(2).mean()

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    return loss.item()

################################################################################
############################ SET UP AND PARAMETERS #############################
################################################################################

# set up env
env = gym.make("LunarLander-v3", render_mode="rgb_array_list")
state_dim = env.observation_space.shape[0]
action_dim = env.action_space.n


# make the Q and the target network
q_network = QNetwork(state_dim, action_dim)
target_network = QNetwork(state_dim, action_dim)
target_network.load_state_dict(q_network.state_dict()) # ensure the target network is initialized with the same weights as the Q network

epsilon = 1.0  # Exploration rate
epsilon_decay = 0.995 # decay rate of epsilon
min_epsilon = 0.01 # minimum value of epsilon
gamma = 0.99  # Discount factor
batch_size = 64 # number of samples in a batch
replay_buffer = ReplayBuffer(10000)
optimizer = optim.Adam(q_network.parameters()) # specify the optimizer
num_episodes = 1000
target_update_frequency = 10 # update the target network every 10 episodes
print_interval = 20 
episode_rewards = [] # list to store the rewards of each episode
avg_q_values = [] # list to store the average q-values of each episode
losses = [] # list to store the losses of each episode
recording_interval = 100 # record the video on each n-th episode

# enable recording on each recording_interval-th episode (this form of recording has been deprecated)
env = RecordVideo(env, video_folder="Reocrdings/DQN", name_prefix="DQN",
                  episode_trigger=lambda x: x % recording_interval == 0) 
# env = RecordEpisodeStatistics(env) // adds some stats in the form of json regarding the video that is being saved

################################################################################
############################## MAIN TRAINING LOOP ##############################
################################################################################

for episode in range(num_episodes):
    state, _ = env.reset()
    done = False
    episode_reward = 0
    episode_q_values = []
    episode_losses = []

    while not done:
        if np.random.random() < epsilon:
            action = env.action_space.sample()  # Random action
        else:
            with torch.no_grad():
                q_values = q_network(torch.FloatTensor(np.array(state)))
                action = q_values.argmax().item()  # Greedy action
                episode_q_values.append(q_values.mean().item())

        next_state, reward, terminated, truncated, _ = env.step(action)
        done = terminated or truncated
        episode_reward += reward
        replay_buffer.push(state, action, reward, next_state, done)
        state = next_state

        if replay_buffer.size() > batch_size:
            batch = replay_buffer.sample(batch_size)
            loss = train_q_network(q_network, target_network, batch, gamma, optimizer)
            episode_losses.append(loss)

        if done:
            epsilon = max(min_epsilon, epsilon * epsilon_decay)

    # Update the target network periodically
    if episode % target_update_frequency == 0:
        target_network.load_state_dict(q_network.state_dict())

    # below are used for recording the episode stats
    ############################################################################
    episode_rewards.append(episode_reward)
    avg_q_values.append(np.mean(episode_q_values) if episode_q_values else 0)
    losses.append(np.mean(episode_losses) if episode_losses else 0)

    # Print stats based on the control: print_interval
    if (episode + 1) % print_interval == 0:
        avg_reward = np.mean(episode_rewards[-print_interval:])
        avg_q = np.mean(avg_q_values[-print_interval:])
        avg_loss = np.mean(losses[-print_interval:])
        print(f"Episode {episode + 1}/{num_episodes}")
        print(f"Avg Reward: {avg_reward:.2f}")
        print(f"Avg Q-value: {avg_q:.2f}")
        print(f"Avg Loss: {avg_loss:.4f}")
        print(f"Epsilon: {epsilon:.2f}")
        print("--------------------")

env.close()
################################################################################
############################## END OF TRAINING #################################
################################################################################
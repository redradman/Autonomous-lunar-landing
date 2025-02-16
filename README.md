# Autonomous-lunar-landing
Auto-Pilot / LunarLander-v3** is a reinforcement learning project that leverages [Deep Q-Network (DQN) algorithm](https://arxiv.org/abs/1312.5602) to **train an autonomous agent to land a ship safely without collision**. 

Utilizing the [LunarLander-v3](https://gymnasium.farama.org/environments/box2d/lunar_lander/) environment from Gymnasium, the agent must learn to land the ship in the designated spot without crashing into the two yellow flags. **The agent learns how to do this using the rewards (numeric feedback) it receives for its actions.**

## Table of Contents
- [Autonomous-lunar-landing](#autonomous-lunar-landing)
  - [Table of Contents](#table-of-contents)
  - [Results](#results)
  - [Features](#features)
  - [Environment](#environment)
    - [What the learning agent can see](#what-the-learning-agent-can-see)
    - [What the agent can do](#what-the-agent-can-do)
  - [Experimentation](#experimentation)
  - [Installation](#installation)

## Results
| Before Training | After Training |
|:---:|:---:|
| <img src="https://github.com/user-attachments/assets/33378ccf-7007-491e-b975-2b27104c1f4b" width="380"> | <img src="https://github.com/user-attachments/assets/197f85b4-28b6-4515-8333-4e9521a7109f" width="380"> |
| **Episode 0** <br> The ship simply collapses since the agent has not interacted with the environment and not learned anything yet | **Epsiode 500** <br> The agent has learned to slowly land the ship between the yellow flags|

_Note: Episode refers to training iteration in the context of this project and Reinforcement Learning._

## Features
- **Deep Q-Network (DQN) Implementation**: Customizable DQN target network for stable learning. **In this project,DQN algorithm has been implemented from scratch without any dependencies** from the [original paper](https://arxiv.org/abs/1312.5602) (look at algorithm 1 in the paper for the pseudocode).
- **Advanced Replay Buffer Management**: Enhanced buffer training frequency to optimize learning rates. Replay buffer is used to store the experiences of the agent during training.
- **Comprehensive Documentation**: Detailed README with environment setup, feature descriptions, and usage guidelines.
- **Performance Logging and Visualization**: Track training progress and visualize results for better insights.

## Environment
The environment is a [LunarLander-v3](https://gymnasium.farama.org/environments/box2d/lunar_lander/) from Gymnasium.

### What the learning agent can see
This table provides a detailed description of the key features used in the lander environment, which are critical for controlling and observing the state of the lander during its descent and landing. 

| Index | Feature                                                           | Description                                         |
| ----- | ----------------------------------------------------------------- | --------------------------------------------------- |
| 0     | **Horizontal pad coordinate (x)**                                 | Horizontal position of the lander (x-axis)          |
| 1     | **Vertical pad coordinate (y)**                                   | Vertical position of the lander (y-axis)            |
| 2     | **Horizontal speed (x)**                                          | Speed of the lander along the x-axis                |
| 3     | **Vertical speed (y)**                                            | Speed of the lander along the y-axis                |
| 4     | **Angle**                                                         | Rotation angle of the lander                        |
| 5     | **Angular speed**                                                 | Rotational speed of the lander                      |
| 6     | **If the left leg contact point has touched the land (boolean)**  | Whether the left leg has made contact (True/False)  |
| 7     | **If the right leg contact point has touched the land (boolean)** | Whether the right leg has made contact (True/False) |

### What the agent can do
This table outlines the possible actions the agent (who is learning) can take during the descent and landing of the ship. 

| Index | Action                            | Description                             |
| ----- | --------------------------------- | --------------------------------------- |
| 0     | **Do nothing**                    | The lander remains idle                 |
| 1     | **Fire left orientation engine**  | Rotates the lander to the right         |
| 2     | **Fire the main engine**          | Fires the main engine to propel upwards |
| 3     | **Fire right orientation engine** | Rotates the lander to the left          |

## Experimentation
The `recordings` directory contains the videos of the agent's performance in the training process. The recordings happen every 100 episodes.

To observe the effects of the buffer reply, the usage of the buffer reply was modified with another training iteration heavily dependent on the buffer. This hindered the learning process and the agent was unable to learn anything stable. If you are interested in observing this check out the `recordings` directory and compare the "regular" training with the "buffer" training.

## Installation
To run the DQN.py file, create a virtual environment and install the dependencies. Here is the command:
```bash
python -m venv venv
source venv/bin/activate
pip install "gymnasium[all]" torch numpy
```

If you would like to run the PPO model instead of the DQN model, you should also install the stable-baselines3 library:
```bash
python -m venv venv
source venv/bin/activate
pip install "gymnasium[all]" torch numpy stable-baselines3
```

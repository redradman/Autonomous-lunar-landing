# Auto-Pilot / LunarLander-v3

## Table of Contents
- [Auto-Pilot / LunarLander-v3](#auto-pilot--lunarlander-v3)
  - [Table of Contents](#table-of-contents)
  - [Project Overview](#project-overview)
  - [Features](#features)
  - [Results](#results)
  - [Environment](#environment)
    - [Lander State Features](#lander-state-features)
    - [Lander Actions](#lander-actions)
  - [Installation](#installation)

## Project Overview

**Auto-Pilot / LunarLander-v3** is a reinforcement learning project that leverages Deep Q-Network (DQN) algorithm to train an autonomous agent to land a ship safely without collision. Utilizing the [LunarLander-v3](https://gymnasium.farama.org/environments/box2d/lunar_lander/) environment from Gymnasium, this project demonstrates the application of Deep Q-Networks (DQN) and Proximal Policy Optimization (PPO) in training agents to perform complex landing maneuvers with high efficiency and stability.


## Features
- **Deep Q-Network (DQN) Implementation**: Customizable DQN with replay buffer and target network for stable learning. DQN has been implemented from scratch from the [original paper](https://arxiv.org/abs/1312.5602) (look at algorithm 1 in the paper for the pseudocode).
- **Proximal Policy Optimization (PPO)**: Integration with Stable Baselines 3 for policy-based reinforcement learning. PPO's original paper can be found [here](https://arxiv.org/abs/1707.06347).
- **Advanced Replay Buffer Management**: Enhanced buffer training frequency to optimize learning rates.
- **Comprehensive Documentation**: Detailed README with environment setup, feature descriptions, and usage guidelines.
- **Performance Logging and Visualization**: Track training progress and visualize results for better insights.

## Results



## Environment
The environment is a [LunarLander-v3](https://gymnasium.farama.org/environments/box2d/lunar_lander/) from Gymnasium.


### Lander State Features

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

### Lander Actions

This table outlines the possible actions the lander can take during its descent and landing. 

| Index | Action                            | Description                             |
| ----- | --------------------------------- | --------------------------------------- |
| 0     | **Do nothing**                    | The lander remains idle                 |
| 1     | **Fire left orientation engine**  | Rotates the lander to the right         |
| 2     | **Fire the main engine**          | Fires the main engine to propel upwards |
| 3     | **Fire right orientation engine** | Rotates the lander to the left          |



## Installation


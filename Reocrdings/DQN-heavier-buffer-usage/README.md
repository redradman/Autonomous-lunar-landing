In this variation of the DQN algorithm here are the modifications that have been made to the DQN code:

### Changes

A new variable was added to the `DQN.py` file in params section:

```python
train_probability = 0
```

This variable controls the frequency of training on the buffer. It is initilized to 0 and then changed to 0.8 after the first time that the buffer training has been completed (this is to prevent sampling larger batch from the buffer than what is already inside it). After that the variable is set to 0.8 to havily increase the frequency of training on the buffer.

Inside the for training loop there was a changed to:

```python
if replay_buffer.size() > batch_size or np.random.random() < train_probability:
    train_probability = 0.8
    batch = replay_buffer.sample(batch_size)
    loss = train_q_network(q_network, target_network, batch, gamma, optimizer)
    episode_losses.append(loss)
```

### Results

Instead of the lander landing the designated safe zone, it now simply hovering in place and does not move much look at episodes 300, 400, and 500. Finally, in the last episode (900) the lander fails to land and crashes. This shows the unstability associated with high frequency training on the buffer.

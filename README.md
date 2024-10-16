# Apollos-Touch / LunarLander-v3

## Lander State Features

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

## Lander Actions

This table outlines the possible actions the lander can take during its descent and landing.

| Index | Action                            | Description                             |
| ----- | --------------------------------- | --------------------------------------- |
| 0     | **Do nothing**                    | The lander remains idle                 |
| 1     | **Fire left orientation engine**  | Rotates the lander to the right         |
| 2     | **Fire the main engine**          | Fires the main engine to propel upwards |
| 3     | **Fire right orientation engine** | Rotates the lander to the left          |

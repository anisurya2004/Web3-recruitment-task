# Web3-recruitment-task
## Overview
This file contains a Car class which tracks the movement of the car in 2-D and there are methods which can detect if two cars in space have collided and return the time to collision of two cars using the coordinates and speed. The car has been considered to be a point particle and calculations have been done accordingly.

## Attributes
***make***(string) : make of the car

***model***(string) : model of the car

***year***(int) : year the car was made

***speed_x***(int) : current speed in x direction

***speed_y***(int) : current speed in y direction

***x***(int) : x coordinate of the car

***y***(int) : y coordinate of the car

## Methods
***accelerate(speed_increment)*** : increases the speed of the car in the direction the car was already moving

***brake(speed_decrement)*** : decreases the speed of the car in the direction the car was already moving

***detect_collision(car2)*** : returns true if both the x and y coordinates of the cars are same, else false

***time_to_collision(car2)*** : returns time to collision by finding the relative velocity. If the two cars won't collide if they keep moving on with the same speed then it will return -1.

***move()*** : moves the car in x and y coordinates according to the speeds in respective directions

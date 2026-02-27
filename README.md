# Robotlibrary for Raspberry Pi Pico
## Project description
This is a library written in micropython for robots based on the Raspberry Pi Pico. The follwing sensors / parts can be used with this: 
+ ultrasonic sensor
+ infrared sensor
+ servo motor that turns the ultrasonic sensor for sweeps of the surroundings.
+ the motors of course
+ a remote control via bluetooth can be connected. 2 types are available: 1 with a slider for speed and two rotary encoders, one with a joystick.
+ a bluetooth library that handles the connections. 
## Types of robots
+ a modified SMARS robot
+ a crawling robot that moves like a turtle
+ a four-legged robot that moves like a dog
+ a line following robot. Implementation of PID algorithm not finished yet. 
Detailed description is available on: [Jb Knowledgebase](https://bookstack.jb-net.eu/books/robotik) (Only in German)

## Installation and running
Rename the unpacked folder *robotlibrary* and copy it to the Raspberry Pi Pico. To use the robots, import the main class of the robot you want to use: 

+ `from robotlibrary.robot import Robot` for the SMARS robot (or any robot with wheels).
+ `from robotlibrary.crawly import Crawly` for the turtle like robot. 
+ `from robotlibrary.walky import Walky` for the dog like robot. 

In each file you can also find example code to get you started. 

### Needed parts
Apart from the Raspberry Pi Pico you will need an ultrasonic sensor, a motor driver, two motors and an energy source. There are so many possibilities on how to do this that I won't describe them here. 

## Some advice
This whole project is for my robotics classes, so all of that goes with lessons and help from me. If you know what you are doing you can certainly try this for yourself as well. 

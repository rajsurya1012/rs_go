# 4-Wheeled Robot Simulation and Autonomous Navigation

**Author:** Raj Surya

## Overview

This repository contains a simulation of a 4-wheeled robot designed using Fusion 360 and controlled via ROS (Robot Operating System). This project was a crucial part of my early undergraduate years, serving as a test platform for learning and experimenting with various robotics concepts, including control systems, SLAM for mapping and localization, and autonomous navigation.

## Robot Design

![Robot Design](https://github.com/rajsurya1012/rs_go/raw/main/rs_go.png)

The robot is designed in Fusion 360 and features a differential drive system, allowing for precise movement and control. It is equipped with mounts for LIDAR and camera sensors, essential for navigation and environment perception.

## Features

- **Differential Drive Control:** Enables precise movement of the robot through speed variations of individual wheels.
- **SLAM Integration:**
  - **GMapping:** For creating maps of the environment.
  - **AMCL (Adaptive Monte Carlo Localization):** For robust localization and autonomous navigation.
- **Sensor Integration:**
  - **LIDAR:** For obstacle detection and distance measurement.
  - **Camera:** For visual processing and environment perception.
- **Navigation Algorithms:**
  - **Bug0 Algorithm:** Simple obstacle avoidance strategy.
  - **Wall Following Algorithm:** Maintains a constant distance from walls for navigation in constrained environments.

## Autonomous Navigation

The robot's autonomous navigation capabilities are visualized in the following map:

![Autonomous Navigation Map](https://github.com/rajsurya1012/rs_go/raw/main/map/navigation.png)

## Learning and Exploration

This project was instrumental in my journey of learning ROS and exploring robotics. It provided hands-on experience with designing, controlling, and navigating a robot in a simulated environment, laying the foundation for more advanced projects in the future.

## Getting Started

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/rajsurya1012/rs_go.git

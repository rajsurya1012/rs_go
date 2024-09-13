# 4-Wheeled Robot Simulation and Autonomous Navigation

**Author:** Raj Surya

## Overview

This repository contains a simulation of a 4-wheeled robot designed using Fusion 360 and controlled via ROS (Robot Operating System). It serves as a test platform for learning and experimenting with various robotics concepts, including control systems, SLAM for mapping and localization, and autonomous navigation.

## Features

- **Fusion 360 Model:** A custom-designed 4-wheeled robot with differential drive capabilities.
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

## Components

### Robot Design

- Developed in Fusion 360, the robot model includes:
  - Four wheels for differential drive
  - Mounts for LIDAR and camera sensors

### Control and Navigation

- **Differential Drive System:** Allows the robot to maneuver by adjusting wheel speeds.
- **SLAM (Simultaneous Localization and Mapping):** Utilizes GMapping and AMCL to create and navigate maps of the environment, enabling autonomous operation.

### Sensor Integration

- **LIDAR:** Provides real-time obstacle detection and distance measurement.
- **Camera:** Captures visual data for processing and navigation.

### Algorithms

- **Bug0 Algorithm:** Implements basic obstacle avoidance by following a path and navigating around obstacles.
- **Wall Following Algorithm:** Enables navigation by maintaining a set distance from walls. Experimented with autonomous mapping using wall following algorihtm.

## Getting Started

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/rajsurya1012/rs_go.git

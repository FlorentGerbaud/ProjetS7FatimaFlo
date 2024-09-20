# Simple Road Traffic Modeling (SRTM)

## Overview
This project, titled Simple Road Traffic Modeling, was carried out by Florent Gerbaud and Fatima Ezzahra Rharrour at Polytech Nice-Sophia as part of their MAM4 program. The project focuses on modeling road traffic using both microscopic and macroscopic approaches, analyzing vehicle behavior and traffic flow dynamics.

The main objectives of this project were:
- Developing traffic flow models using Ordinary Differential Equations (ODE) and Partial Differential Equations (PDE).
- Simulating traffic conditions under different driver behaviors and traffic densities.
- Studying the stability and equilibrium of traffic systems under various conditions.

## Project Structure

### Code Organization
The project uses GitHub to organize the codebase. Branches were created to handle different tasks simultaneously. The following directories are included:
- `/MicroscopicModels`: Contains the ODE-based models for simulating vehicle behavior.
- `/MacroscopicModels`: Contains PDE-based models simulating traffic as a fluid.
- `/Simulations`: Python scripts to run various simulations (accordion phenomenon, drunk drivers, etc.).
- `/Documentation`: Report and additional files documenting the project, including theoretical derivations and references.
- `/Tests`: Test cases for verifying the accuracy of the implemented models.

### Models Implemented
- **Linear Model (Microscopic)**: A simple follow-the-leader approach where each car adjusts its speed based on the car in front.
- **Newell’s Model (Microscopic)**: A more realistic traffic model that considers the speed and acceleration of adjacent vehicles.
- **Euler’s Explicit Method (Macroscopic)**: A PDE-based model to simulate traffic flow under low density.
- **Lax-Friedrich’s Method (Macroscopic)**: A PDE-based model that handles high-density traffic flow to avoid instabilities.

### Simulations

#### Microscopic Simulations
- **Accordion Phenomenon**: Simulates two or more cars following each other at varying speeds.
- **Drunk Drivers**: Introduces random variations in acceleration to simulate the behavior of intoxicated drivers.
- **Unpredictable Drivers**: Models erratic driving behaviors with sudden accelerations and decelerations.
- **Accidents**: Simulates collisions due to delayed reactions or high speeds.

#### Macroscopic Simulations
- **Traffic Flow Using Euler's Explicit Method**: Models traffic as a fluid with low density, showing the formation of traffic waves.
- **Traffic Flow Using Lax-Friedrich's Method**: Handles high-density traffic, showing jam formation and dissipation.

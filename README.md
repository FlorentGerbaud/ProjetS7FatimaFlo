# Simple Road Traffic Modeling (SRTM)

// add Table of Contents
## Table of Contents
1. [Overview](#overview)
2. [Project Structure](#project-structure)
    - [Code Organization](#code-organization)
    - [Models Implemented](#models-implemented)
    - [Simulations](#simulations)
        - [Microscopic Simulations](#microscopic-simulations)
        - [Macroscopic Simulations](#macroscopic-simulations)
    - [Launching a Test Case](#launching-a-test-case)
        - [Name of the Test Case](#name-of-the-test-case)
3. [Contributors](#contributors)
4. [License](#license)
      

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

## Launching a Test Case

To launch a test case, follow these steps:

1. Navigate to the "SRTM" directory.
2. Choose between "EDO" or "EDP" depending on your requirements.
3. Select the appropriate model type.
4. Locate the "CasTestToLaunch" folder.
5. Inside "CasTestToLaunch," find "TestToLaunch."
6. Choose the number of cars for the model if you choose EDO method.
7. Select a specific test case.
8. Run the corresponding `.bat` file.

### Name of the Test Case

The test case names are structured as follows:

#### For the ODE Method:

**Parameters for the test case:**
- `CV` := Convergence
- `DV` := Divergence
- `Acc` := Acceleration
- `D` := Drunk
- `I` := Unpredictable
- `Aco` := Accordion
- `O` := Obstacle
- `CA` := Car Accident

**Naming Convention:**
- For the linear model: `Model1W{X}C_{a}_{b}...{z}`
  - `{X}`: Number of cars
  - `{a}`, `{b}`, ..., `{z}`: Parameters for the test case

- For Newell's model: `Model1W{X}C_{a}_{b}...{z}`
  - `{X}`: Number of cars
  - `{a}`, `{b}`, ..., `{z}`: Parameters for the test case

**Example:**

- `Model1W2C_Acc_CA` := Linear model with 2 cars and a driver that accelerates and causes a car accident

#### For the PDE Method:

**Parameters for the test case:**
- `IC` := Initial condition
- `G` := Gaussian
- `S` := Sinusoidal
- `T` := Triangle
- `P` := Pulse function
- `C` := Constant

**Naming Convention:**
- For both cases, the name of the test case is: `Modele_IC_{X}`
  - `{X}`: Initial condition

**Example:**
- `Modele_IC_G` := Gaussian initial condition

## Contributors

- Florent Gerbaud
- Fatima Ezzahra Rharrour
- Polytech Nice-Sophia
- MAM4 Program


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


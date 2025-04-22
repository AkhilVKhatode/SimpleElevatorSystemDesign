# SimpleElevatorSystemDesign

The Elevator System simulates the working of a building's elevator mechanism, including request handling, elevator movement, and decision-making based on proximity and direction. It follows object-oriented principles and models core components such as Elevators, Controllers, and Request management.

## Design Principles

- Object-Oriented Design
- Separation of Concerns (Elevator vs Controller)
- Enum-based State Management (Direction and DoorStatus)
- Simulated Time-Step Execution
- Scalable for extension (e.g., priority-based scheduling, capacity handling)

## Components

### 1. `Elevator` Class
- Manages individual elevator behavior: movement, opening/closing doors, processing floor requests.
- Maintains internal state including direction, current floor, and pending requests.

### 2. `ElevatorController` Class
- Handles elevator assignment for incoming requests.
- Implements a basic scheduling logic (idle elevator closest to request).
- Can be extended for more advanced scheduling policies.

### 3. `Direction` and `DoorStatus` Enums
- Clearly represent elevator direction and door state.

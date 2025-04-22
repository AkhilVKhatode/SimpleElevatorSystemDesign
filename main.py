from enum import Enum
import heapq

# Enums for direction and door status
class Direction(Enum):
    UP = 1
    DOWN = -1
    IDLE = 0

class DoorStatus(Enum):
    OPEN = 1
    CLOSED = 0

# Elevator class
class Elevator:
    def __init__(self, id, max_floor, capacity=8):
        self.id = id
        self.current_floor = 0
        self.direction = Direction.IDLE
        self.door_status = DoorStatus.CLOSED
        self.requests = []
        self.max_floor = max_floor
        self.capacity = capacity
        self.passengers = 0

    def move(self):
        if self.requests:
            next_floor = self.requests[0]
            if self.current_floor < next_floor:
                self.direction = Direction.UP
                self.current_floor += 1
            elif self.current_floor > next_floor:
                self.direction = Direction.DOWN
                self.current_floor -= 1
            else:
                self.open_door()
                self.requests.pop(0)
                self.close_door()
        else:
            self.direction = Direction.IDLE

    def open_door(self):
        self.door_status = DoorStatus.OPEN
        print(f"Elevator {self.id} opening doors at floor {self.current_floor}")

    def close_door(self):
        self.door_status = DoorStatus.CLOSED
        print(f"Elevator {self.id} closing doors")

    def add_request(self, floor):
        if floor not in self.requests:
            self.requests.append(floor)
            self.requests.sort()

# Controller class
class ElevatorController:
    def __init__(self, num_elevators=3, max_floor=15):
        self.elevators = [Elevator(i, max_floor) for i in range(num_elevators)]
        self.max_floor = max_floor

    def request_elevator(self, floor, direction):
        # Simple logic: choose the first idle elevator or the one closest to the requested floor
        best_elevator = None
        min_distance = self.max_floor + 1
        for elevator in self.elevators:
            if elevator.direction == Direction.IDLE:
                distance = abs(elevator.current_floor - floor)
                if distance < min_distance:
                    min_distance = distance
                    best_elevator = elevator
        if best_elevator:
            best_elevator.add_request(floor)
            print(f"Elevator {best_elevator.id} assigned to floor {floor}")
        else:
            print(f"No available elevator for floor {floor} at the moment")

    def step(self):
        for elevator in self.elevators:
            elevator.move()

# Example usage
if __name__ == "__main__":
    controller = ElevatorController()
    controller.request_elevator(5, Direction.UP)
    controller.request_elevator(3, Direction.DOWN)
    for _ in range(10):
        controller.step()

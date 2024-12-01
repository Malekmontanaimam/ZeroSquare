

class Astar:
    def __init__(self, initial_state):
        self.initial_state = initial_state

    def heauristic(self, current, goal):
        return abs(current[0] - goal[0]) + abs(current[1] - goal[1])



class SteepestHillClimping:
    def __init__(self, initial_state):
        self.initial_state = initial_state

    def solve(self):
        current_state = self.initial_state
        current_path = []
        visited = set()
        visited.add(self._hash_state(current_state))

        while True:
            print("Current path:", current_path)
            print("Current state heuristic:", self.heuristic(current_state))
            current_state.grid.print_grid()

            if current_state.grid.is_goal_state():
                print("Goal state reached!")
                return current_path


            best_neighbor = None
            best_heuristic = float("inf")
            best_move = None

            for next_state, move, move_cost in self.get_next_states(current_state):
                state_hash = self._hash_state(next_state)
                if state_hash not in visited:
                    visited.add(state_hash)
                    h_value = self.heuristic(next_state)
                    if h_value < best_heuristic:
                        best_neighbor = next_state
                        best_heuristic = h_value
                        best_move = move

            if best_neighbor is None or best_heuristic >= self.heuristic(current_state):

                print("Stuck at local optimum or no neighbors found.")
                return None


            current_state = best_neighbor
            current_path.append(best_move)

    def get_next_states(self, state):
        next_states = []
        for x, y in state.grid.selected_squares:
            for direction in ["up", "down", "left", "right"]:
                new_state = state.move_square(x, y, direction)
                if new_state:
                    move_cost = 1
                    next_states.append((new_state, direction, move_cost))
        return next_states

    def heuristic(self, state):
        total_distance = 0
        for x, y in state.grid.selected_squares:
            goal_x, goal_y = state.grid.goal_position
            total_distance += abs(x - goal_x) + abs(y - goal_y)
        return total_distance

    def _hash_state(self, state):
        return tuple(tuple((square.square_type, square.color) for square in row) for row in state.grid.grid)

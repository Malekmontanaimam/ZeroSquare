import heapq

class UCS:
    def __init__(self, initial_state):
        self.initial_state = initial_state

    def solve(self):

        priority_queue = [(0, self.initial_state, [])]#(cost, state, path)
        visited = set()
        visited.add(self._hash_state(self.initial_state))

        while priority_queue:
            cost, current_state, path = heapq.heappop(priority_queue)

            print("Current path:", path)
            print("Current cost:", cost)
            print("Is goal state?", current_state.grid.is_goal_state())
            current_state.grid.print_grid()

            if current_state.grid.is_goal_state():
                print("Goal state reached with cost:", cost)
                return path

            for next_state, move, move_cost in self.get_next_states(current_state):
                state_hash = self._hash_state(next_state)
                if state_hash not in visited:
                    visited.add(state_hash)
                    heapq.heappush(priority_queue, (cost + move_cost, next_state, path + [move]))

        print("No solution found")
        return None

    def get_next_states(self, state):
        next_states = []
        for x, y in state.grid.selected_squares:
            for direction in ["up", "down", "left", "right"]:
                new_state = state.move_square(x, y, direction)
                if new_state:
                    move_cost = 1
                    next_states.append((new_state, direction, move_cost))
        return next_states

    def _hash_state(self, state):
        return tuple(tuple(square.square_type for square in row) for row in state.grid.grid)

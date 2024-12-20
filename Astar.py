import heapq

class Astar:
    def __init__(self, initial_state):
        self.initial_state = initial_state

    def solve(self):
        # (total_cost, g_cost, state, path)
        priority_queue = [(self.heuristic(self.initial_state), 0, self.initial_state, [])]
        visited = set()
        visited.add(self._hash_state(self.initial_state))

        while priority_queue:
            total_cost, g_cost, current_state, path = heapq.heappop(priority_queue)

            print("Current path:", path)
            print("Current g_cost:", g_cost)
            print("Is goal state?", current_state.grid.is_goal_state())
            current_state.grid.print_grid()

            if current_state.grid.is_goal_state():
                print("Goal state reached with cost:", g_cost)
                print("Is goal state?", current_state.grid.is_goal_state())
                return path

            for next_state, move, move_cost in self.get_next_states(current_state):
                state_hash = self._hash_state(next_state)
                if state_hash not in visited:
                    visited.add(state_hash)
                    new_g_cost = g_cost + move_cost
                    new_total_cost = new_g_cost + self.heuristic(next_state)
                    heapq.heappush(priority_queue, (new_total_cost, new_g_cost, next_state, path + [move]))

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

    def heuristic(self, state):
        total_distance = 0
        for x, y in state.grid.selected_squares:
            goal_x, goal_y = state.grid.goal_position
            total_distance += abs(x - goal_x) + abs(y - goal_y)
        return total_distance

    def _hash_state(self, state):
        return tuple(tuple(square.square_type for square in row) for row in state.grid.grid)

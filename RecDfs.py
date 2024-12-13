class RecDfs:
    def __init__(self, initial_state):
        self.initial_state = initial_state

    def solve(self):
        visited = set()


        def dfs(current_state, path):

            print("Current path:", path)
            print("Is goal state?", current_state.grid.is_goal_state())
            current_state.grid.print_grid()


            if current_state.grid.is_goal_state():
                print("Goal state reached:", path)
                return path


            visited.add(self._hash_state(current_state))


            for next_state, move in self.get_next_states(current_state):
                state_hash = self._hash_state(next_state)
                if state_hash not in visited:

                    result = dfs(next_state, path + [move])
                    if result:
                        return result


            return None


        return dfs(self.initial_state, [])

    def get_next_states(self, state):
        next_states = []
        for x, y in state.grid.selected_squares:
            for direction in ["up", "down", "left", "right"]:
                new_state = state.move_square(x, y, direction)
                if new_state:
                    next_states.append((new_state, direction))
        return next_states

    def _hash_state(self, state):
        return tuple(tuple((square.square_type, square.color) for square in row) for row in state.grid.grid)

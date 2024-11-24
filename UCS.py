import heapq

from pygame.mixer_music import queue

from State import *
class UCS :
    def __init__(self, initial_state):
        self.initial_state = initial_state
        queue=[]
        new_cost=0

    def solve(self):
        heapq.heappush(queue, (0, self.initial_state))
        visited = set()
        while queue:

            current_cost, current_node,path  = heapq.heappop(queue)

            print("Current path:", path)
            current_state.grid.print_grid()
            print("Is goal state?", current_state.grid.is_goal_state())

            if current_state.grid.is_goal_state():
                 print("Goal state reached:", path)
                 return path

            for next_state, move in self.get_next_states(current_state):
                  state_hash = self._hash_state(next_state)
                 if state_hash not in visited:
                     visited.add(state_hash)
                     queue.append((next_state, path + [move]))
                     print("No solution found")
                     return None


     def get_next_states(self, state):
             next_states = []
             for x, y in state.grid.selected_squares:
                for direction in ["up", "down", "left", "right"]:
                    new_state = state.move_square(x, y, direction)
                    if new_state:
                         new_cost= 1
                         heapq.heappush(queue, (new_cost, new_state))
                         next_states.append((new_state, direction))
                    return next_states


    print("Priority Queue after exploration:", queue)













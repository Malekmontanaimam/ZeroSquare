import copy
import pygame
import sys
from Square import *
RED = (255, 0, 0)
RED2 = (255, 4, 190)
class State:

    def __init__(self, grid):
        self.grid = copy.deepcopy(grid)

    def __lt__(self, other):
        return True

    def move_square(self, x, y, direction):
        cost = 0

        if self.grid.grid[x][y].square_type != "movable":
            return None

        new_state = State(self.grid)
        square = new_state.grid.grid[x][y]
        new_state.grid.grid[x][y] = Square("empty", WHITE)

        # منطق الحركة حسب الاتجاهات
        if direction == "up":
            while x > 0 and (new_state.grid.grid[x - 1][y].square_type == "empty" or new_state.grid.grid[x - 1][
                y].square_type == "weak"):
                x -= 1
                cost += 1
                if (x, y) == new_state.grid.goal_position and square.color == RED:
                    break
                if (x, y) == new_state.grid.goal_position1 and square.color == RED2:
                    break
        elif direction == "down":
            while x < new_state.grid.size - 1 and (
                    new_state.grid.grid[x + 1][y].square_type == "empty" or new_state.grid.grid[x + 1][
                y].square_type == "weak"):
                x += 1
                cost += 1
                if (x, y) == new_state.grid.goal_position and square.color == RED:
                    break
                if (x, y) == new_state.grid.goal_position1 and square.color == RED2:
                    break
        elif direction == "left":
            while y > 0 and (new_state.grid.grid[x][y - 1].square_type == "empty" or new_state.grid.grid[x][
                y - 1].square_type == "weak"):
                y -= 1
                cost += 1
                if (x, y) == new_state.grid.goal_position and square.color == RED:
                    break
                if (x, y) == new_state.grid.goal_position1 and square.color == RED2:
                    break
        elif direction == "right":
            while y < new_state.grid.size - 1 and (
                    new_state.grid.grid[x][y + 1].square_type == "empty" or new_state.grid.grid[x][
                y + 1].square_type == "weak"):
                y += 1
                cost += 1
                if (x, y) == new_state.grid.goal_position and square.color == RED:
                    break
                if (x, y) == new_state.grid.goal_position1 and square.color == RED2:
                    break

        if new_state.grid.grid[x][y].square_type == "weak":
            print("Restart.")
            pygame.quit()
            sys.exit()

        new_state.grid.grid[x][y] = square
        new_state.grid.selected_squares.append((x, y))

        return new_state

    def next_states(self):
        next_states = []
        for x, y in self.grid.selected_squares:
            for direction in ["up", "down", "left", "right"]:
                new_state = self.move_square(x, y, direction)
                if new_state:
                    next_states.append(new_state)
        return next_states

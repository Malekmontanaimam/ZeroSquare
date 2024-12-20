import copy
import pygame
import sys
from Square import *
RED = (255, 0, 0)
RED2 = (255, 4, 190)
YELLOW = (255, 255, 0)
Marron =  (128, 0, 0)
TEAL = (0, 128, 128)
class State:

    def __init__(self, grid):
        self.grid = copy.deepcopy(grid)



    def move_square(self, x, y, direction):
        cost = 0

        if self.grid.grid[x][y].square_type != "movable":
            return None

        new_state = State(self.grid)
        square = new_state.grid.grid[x][y]
        new_state.grid.grid[x][y] = Square("empty", WHITE)


        if direction == "up":
            while x > 0 and (new_state.grid.grid[x - 1][y].square_type == "empty" or new_state.grid.grid[x - 1][
                y].square_type == "weak"):
                x -= 1
                cost += 1

                if ((x, y) == new_state.grid.goal_position and square.color == RED) or \
                        ((x, y) == new_state.grid.goal_position1 and square.color == YELLOW) :
                    #or\
                      #  ((x, y) == new_state.grid.goal_position2 and square.color == RED2) or \
                    #((x, y) == new_state.grid.goal_position3 and square.color == Marron) or \
                     # ((x, y) == new_state.grid.goal_position4 and square.color == TEAL) \


                    break
        elif direction == "down":
            while x < new_state.grid.size - 1 and (
                    new_state.grid.grid[x + 1][y].square_type == "empty" or new_state.grid.grid[x + 1][
                y].square_type == "weak"):
                x += 1
                cost += 1
                if ((x, y) == new_state.grid.goal_position and square.color == RED) or \
                        ((x, y) == new_state.grid.goal_position1 and square.color == YELLOW):
                    # or\
                    #  ((x, y) == new_state.grid.goal_position2 and square.color == RED2) or \
                    # ((x, y) == new_state.grid.goal_position3 and square.color == Marron) or \
                    # ((x, y) == new_state.grid.goal_position4 and square.color == TEAL) \

                    break

        elif direction == "left":
            while y > 0 and (new_state.grid.grid[x][y - 1].square_type == "empty" or new_state.grid.grid[x][
                y - 1].square_type == "weak"):
                y -= 1
                cost += 1
                if ((x, y) == new_state.grid.goal_position and square.color == RED) or \
                        ((x, y) == new_state.grid.goal_position1 and square.color == YELLOW):
                    # or\
                    #  ((x, y) == new_state.grid.goal_position2 and square.color == RED2) or \
                    # ((x, y) == new_state.grid.goal_position3 and square.color == Marron) or \
                    # ((x, y) == new_state.grid.goal_position4 and square.color == TEAL) \

                    break

        elif direction == "right":
            while y < new_state.grid.size - 1 and (
                    new_state.grid.grid[x][y + 1].square_type == "empty" or new_state.grid.grid[x][
                y + 1].square_type == "weak"):
                y += 1
                cost += 1
                if ((x, y) == new_state.grid.goal_position and square.color == RED) or \
                        ((x, y) == new_state.grid.goal_position1 and square.color == YELLOW):
                    # or\
                    #  ((x, y) == new_state.grid.goal_position2 and square.color == RED2) or \
                    # ((x, y) == new_state.grid.goal_position3 and square.color == Marron) or \
                    # ((x, y) == new_state.grid.goal_position4 and square.color == TEAL) \

                    break

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

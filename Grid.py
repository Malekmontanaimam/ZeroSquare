from Square import *
import pygame

GRAY = (150, 150, 150)
GREEN = (0, 255, 0)
CYAN_GREEN = (0, 255, 255)
RED = (255, 0, 0)
RED2 = (255, 4, 190)
BLACK = (0, 0, 0)

SQUARE_SIZE = 50

class Grid:
    def __init__(self, n):
        self.size = n
        self.grid = [[Square("empty", WHITE) for _ in range(n)] for _ in range(n)]
        self.selected_squares = []
        self.goal_position = (self.size - 2, self.size - 2)
        #self.goal_position1 = (self.size - 5, self.size - 2)

        for i in range(n):
            self.grid[0][i] = Square("fixed", GRAY)
            self.grid[n - 1][i] = Square("fixed", GRAY)
            self.grid[i][0] = Square("fixed", GRAY)
            self.grid[i][n - 1] = Square("fixed", GRAY)

    def set_square(self, x, y, square):
        if 0 <= x < self.size and 0 <= y < self.size:
            self.grid[x][y] = square
            if square.square_type == "movable":
                self.selected_squares.append((x, y))

    def find_goal(self):
        return self.goal_position

    def draw_grid(self, screen):
        for i in range(self.size):
            for j in range(self.size):

                if (i, j) == self.goal_position:
                    color = WHITE

                #elif (i, j) == self.goal_position1:
                 #   color = WHITE
                else:
                    square = self.grid[i][j]
                    color = square.color if square.square_type != "empty" else WHITE


                pygame.draw.rect(screen, color, (j * SQUARE_SIZE, i * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))


                if (i, j) == self.goal_position:
                    pygame.draw.rect(screen, RED, (j * SQUARE_SIZE, i * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 5)
                #elif (i, j) == self.goal_position1:
                 #   pygame.draw.rect(screen, RED2, (j * SQUARE_SIZE, i * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 5)


                pygame.draw.rect(screen, BLACK, (j * SQUARE_SIZE, i * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 1)

    def is_goal_state(self):
        all_reached = True
        for x, y in self.selected_squares:

            if (x, y) == self.goal_position and self.grid[x][y].color == RED:
              self.grid[x][y] = Square("empty", WHITE)

          #  elif (x, y) == self.goal_position1 and self.grid[x][y].color == RED2:
           #       self.grid[x][y] = Square("empty", WHITE)

            else:

                all_reached = False


        self.selected_squares = [(x, y) for x, y in self.selected_squares if self.grid[x][y].square_type == "movable"]

        return all_reached and not self.selected_squares

    def print_grid(self):
        symbol_map = {
            "fixed": "⬛",
            "empty": "⬜",
            "movable": "🔴",
        }
        for row in self.grid:
            for square in row:
                print(symbol_map.get(square.square_type, "⬜"), end=" ")
            print()
        print("\n")

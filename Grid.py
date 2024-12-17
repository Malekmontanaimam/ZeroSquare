from Square import *
import pygame

GRAY = (150, 150, 150)
GREEN = (0, 255, 0)
CYAN_GREEN = (0, 255, 255)
RED = (255, 0, 0)
RED2 = (255, 4, 190)
BLACK = (0, 0, 0)

SQUARE_SIZE = 50
YELLOW = (255, 255, 0)
Marron =  (128, 0, 0)
TEAL = (0, 128, 128)
class Grid:
    def __init__(self, n):
        self.size = n
        self.grid = [[Square("empty", WHITE) for _ in range(n)] for _ in range(n)]
        self.selected_squares = []
        #level 10
        self.goal_position = (self.size - 6, self.size - 7)
        self.goal_position1 = (self.size - 7, self.size - 6)
        '''''
        #level 20
        self.goal_position = (self.size - 2, self.size - 2)
        self.goal_position1 = (self.size - 4, self.size - 4)
        self.goal_position2 = (self.size - 2, self.size - 7)
        self.goal_position3= (self.size - 3, self.size - 8)
        self.goal_position4 = (self.size - 2, self.size - 5)
        '''
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
        return self.goal_position,self.goal_position1,self.goal_position2,self.goal_position3,self.goal_position4

    def draw_grid(self, screen):
        for i in range(self.size):
            for j in range(self.size):
                if (i, j) == self.goal_position:
                    color = WHITE
                elif (i, j) == self.goal_position1:
                   color = WHITE

                else:
                    square = self.grid[i][j]
                    color = square.color if square.square_type != "empty" else WHITE


                pygame.draw.rect(screen, color, (j * SQUARE_SIZE, i * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

                if (i, j) == self.goal_position:
                    pygame.draw.rect(screen, RED, (j * SQUARE_SIZE, i * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 2)
                elif (i, j) == self.goal_position1:
                   pygame.draw.rect(screen, YELLOW, (j * SQUARE_SIZE, i * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 2)
                   '''
                elif (i, j) == self.goal_position2:
                   pygame.draw.rect(screen, RED2, (j * SQUARE_SIZE, i * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 2)
                elif (i, j) == self.goal_position3:
                    pygame.draw.rect(screen, Marron, (j * SQUARE_SIZE, i * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 2)
                elif (i, j) == self.goal_position4:
                    pygame.draw.rect(screen, TEAL, (j * SQUARE_SIZE, i * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 2)
                    '''
                pygame.draw.rect(screen, BLACK, (j * SQUARE_SIZE, i * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 1)

    def is_goal_state(self):
        all_reached = True


        goal_conditions = [
            (self.goal_position, RED),
            (self.goal_position1, YELLOW),
            #(self.goal_position2, RED2),
           # (self.goal_position3, Marron),
            #(self.goal_position4, TEAL),
        ]

        for x, y in self.selected_squares:

            matched = False
            for (goal_x, goal_y), goal_color in goal_conditions:
                if (x, y) == (goal_x, goal_y) and self.grid[x][y].color == goal_color:
                    self.grid[x][y] = Square("empty", WHITE)
                    matched = True
                    break

            if not matched:
                all_reached = False

        self.selected_squares = [
            (x, y) for x, y in self.selected_squares if self.grid[x][y].square_type == "movable"
        ]

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

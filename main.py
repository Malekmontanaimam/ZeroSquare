import pygame
import sys
from Grid import *
from State import *
from Square import *
from BFS import *
from DFS import *
from UCS import *
from RecDfs import *
from Astar import *

WEAK_GRAY = (200, 200, 200)
GRAY = (150, 150, 150)
RED = (255, 0, 0)
RED2 = (255, 4, 190)

SQUARE_SIZE = 50
GRID_SIZE = 7

pygame.init()
screen = pygame.display.set_mode((GRID_SIZE * SQUARE_SIZE, GRID_SIZE * SQUARE_SIZE))
pygame.display.set_caption("Zero Squares Game")
grid = Grid(GRID_SIZE)
grid.set_square(2, 3, Square("fixed", GRAY))
#grid.set_square(6, 1, Square("weak", WEAK_GRAY))
grid.set_square(2, 2, Square("fixed", GRAY))
grid.set_square(1, 5, Square("fixed", GRAY))
grid.set_square(5, 4, Square("fixed", GRAY))
grid.set_square(1, 4, Square("movable", RED))
#grid.set_square(3, 4, Square("movable", RED2))
goal_reached = False

state = State(grid)
bfs_solver = BFS(state)
ucs_solver=UCS(state)
dfs_solver = DFS(state)
recdfs_solver=RecDfs(state)
Astar1=Astar(state)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN and not goal_reached:
            state = State(grid)
            new_state = state

            if event.key == pygame.K_UP:
                for x, y in grid.selected_squares:
                    result_state = new_state.move_square(x, y, "up")
                    if result_state:
                        new_state = result_state
            elif event.key == pygame.K_DOWN:
                for x, y in grid.selected_squares:
                    result_state = new_state.move_square(x, y, "down")
                    if result_state:
                        new_state = result_state
            elif event.key == pygame.K_LEFT:
                for x, y in grid.selected_squares:
                    result_state = new_state.move_square(x, y, "left")
                    if result_state:
                        new_state = result_state
            elif event.key == pygame.K_RIGHT:
                for x, y in grid.selected_squares:
                    result_state = new_state.move_square(x, y, "right")
                    if result_state:
                        new_state = result_state
            elif event.key == pygame.K_s:
                print("Solving using BFS...")
                solution_path = bfs_solver.solve()
                if solution_path:
                    print("Solution path:", solution_path)

            elif event.key == pygame.K_d:
                print("Solving using DFS...")
                solution_path = dfs_solver.solve()
                if solution_path:
                    print("Solution path:", solution_path)
            elif event.key == pygame.K_u:
                print("Solving using UCS...")
                solution_path = ucs_solver.solve()
                if solution_path:
                    print("Solution path:", solution_path)

            elif event.key==pygame.K_r:
                print("Solving using RecDfs...")
                solution_path = recdfs_solver.solve()
                if solution_path:
                    print("Solution path:", solution_path)
            elif event.key==pygame.K_a:
                print("Solving using Astr...")
                solution_path = Astar1.solve()
                if solution_path:
                    print("Solution path:", solution_path)

            if new_state:
                grid = new_state.grid
                grid.print_grid()

    screen.fill(WHITE)
    grid.draw_grid(screen)

    if grid.is_goal_state() and not goal_reached:
        print("Goal achieved!")
        goal_reached = True

    pygame.display.flip()
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
from SteepestHillClimping import *
from SimpleHillClimbing import *
WEAK_GRAY = (200, 200, 200)
GRAY =(150, 150, 150)
RED =(255, 0, 0)
YELLOW =(255, 255, 0)
Marron =(128, 0, 0)
TEAL = (0,128,128)
RED2 = (255, 4, 190)

SQUARE_SIZE = 50
GRID_SIZE = 12#level 10
#GRID_SIZE = 9#level 20
pygame.init()
screen = pygame.display.set_mode((GRID_SIZE * SQUARE_SIZE, GRID_SIZE * SQUARE_SIZE))
pygame.display.set_caption("Zero Squares Game")
grid = Grid(GRID_SIZE)

'''''
grid.set_square(2, 3, Square("fixed", GRAY))
#grid.set_square(6, 1, Square("weak", WEAK_GRAY))
grid.set_square(2, 2, Square("fixed", GRAY))
grid.set_square(1, 5, Square("fixed", GRAY))
grid.set_square(5, 4, Square("fixed", GRAY))
grid.set_square(1, 4, Square("movable", RED))
#grid.set_square(3, 4, Square("movable", RED2))
# المربعات الثابتة



walls = [#level 20
    (1,1),(1,2),(1,3),(1,4),(1,5),(1,6),(1,7),(1,8),(1,9),
    (2,1),(2,2),(2,3),(2,4),(2,5),(2,6),(2,7),(2,8),(2,9),
    (3,1),(3,2),(3,3),(3,4),(3,5),(3,6),(3,7),(3,8),(3,9),
    (4,1),(4,2),(4,3),(4,4),(4,5),(4,6),(4,7),(4,8),(4,9),
    (5, 1),(5, 2),(5, 3), (5, 6), (5, 7),  (5, 10),

    (7,3),(7, 6),
    (8, 2),(8, 4),(8, 5),(8, 9),

]

# المربعات المتحركة
grid.set_square(6, 3, Square("movable", Marron))
grid.set_square(5, 4, Square("movable", TEAL))
grid.set_square(7, 7, Square("movable", YELLOW))
grid.set_square(6, 2, Square("movable", RED2))
grid.set_square(7, 2, Square("movable", RED))
'''''
walls = [#level 10
    (1,1),(1,2),(1,3),(1,4),(1,5),(1,6),(1,7),(1,8),(1,9),(1,10),(1,11),(1,12),
    (2,1),(2,2),(2,3),(2,4),(2,5),(2,6),(2,7),(2,8),(2,9),(2,10),(2,11),(2,12),
    (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8), (3, 9), (3, 10), (3, 11), (3, 12),
    (4, 1),(4, 2),(4, 9), (4, 10),
    (5, 1), (5, 4), (5, 7),  (5, 10),
    (6, 3),(6, 8),
    (7, 5),(7, 8),(7, 9),
    (8, 2),(8, 4),(8, 5),(8, 9),
    (9,4),
    (10, 1), (10, 2), (10, 3), (10, 4), (10, 5), (10, 6), (10, 7), (10, 8), (10, 9), (10, 10), (10, 11), (10, 12),

]
grid.set_square(8, 1, Square("movable", RED))
grid.set_square(8, 10, Square("movable", YELLOW))
for wall in walls:
    grid.set_square(wall[0], wall[1], Square("fixed", GRAY))

goal_reached = False

state = State(grid)
bfs_solver = BFS(state)
ucs_solver=UCS(state)
dfs_solver = DFS(state)
recdfs_solver=RecDfs(state)
Astar1=Astar(state)
SteepestHillClimping=SteepestHillClimping(state)
SimpleHillClimbing=SimpleHillClimbing(state)

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
            elif event.key==pygame.K_h:
                print("Solving using SteepestHillClimping...")
                solution_path = SteepestHillClimping.solve()
                if solution_path:
                    print("Solution path:", solution_path)
            elif event.key==pygame.K_p:
                print("Solving using SimpleHillClimbing...")
                solution_path = SimpleHillClimbing.solve()
                if solution_path:
                    print("Solution path:", solution_path)

            if new_state:
                grid = new_state.grid
                grid.print_grid()

                new_selected_squares = []
                for x, y in grid.selected_squares:
                    if grid.grid[x][y].square_type == "movable":
                        new_selected_squares.append((x, y))
                grid.selected_squares = new_selected_squares
    screen.fill(WHITE)
    grid.draw_grid(screen)

    if grid.is_goal_state() and not goal_reached:
        print("Goal achieved!")
        goal_reached = True

    pygame.display.flip()
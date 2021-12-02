from Robot import *
from MazeProblem import *
from Animation import Animation
from Heuristics import *
from Utilities import *
from Experiments import *


if __name__ == "__main__":
    test_robot(BreadthFirstSearchRobot, [0, 1, 2, 3, 4, 5])
    # test_robot(UniformCostSearchRobot, [0, 1, 2, 3, 4, 5])
    # test_robot(WAStartRobot, [0, 1, 2, 3, 4, 5], heuristic=tail_manhattan_heuristic)
    # test_robot(WAStartRobot, [99], heuristic=tail_manhattan_heuristic)
    # a = solve_and_display(UniformCostSearchRobot, 3)
    # b = solve_and_display(BreadthFirstSearchRobot, 3)

    # for i in range(3):
    #     w_experiment(i)

    # w_values = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
    # for w in w_values:
    #     a = solve_and_display(WAStartRobot, 2, heuristic=center_manhattan_heuristic, w=w, blit=False)
from Robot import *
from MazeProblem import *
from Animation import Animation
from Heuristics import *
from Utilities import *
from Experiments import *

if __name__ == "__main__":
    # test_robot(BreadthFirstSearchRobot, [0, 1, 2, 3, 4, 5])
    # test_robot(UniformCostSearchRobot, [0, 1, 2, 3, 4, 5])
    # test_robot(WAStartRobot, [0, 1, 2, 3, 4, 5], heuristic=tail_manhattan_heuristic)
    test_robot(WAStartRobot, [99], heuristic=tail_manhattan_heuristic)
    a = solve_and_display(WAStartRobot, 99, blit=True, heuristic=tail_manhattan_heuristic)
    # a = solve_and_display(WAStartRobot, 5, blit=True, heuristic=center_manhattan_heuristic)
    # b = solve_and_display(BreadthFirstSearchRobot, 3)

    # for i in range(3):
    #     w_experiment(i)

    # w_values = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
    # for w in w_values:
    #     a = solve_and_display(WAStartRobot, 2, heuristic=center_manhattan_heuristic, w=w, blit=False)

    # for k in [2, 4, 6, 8]:
    #     test_robot(WAStartRobot, [3, 4], heuristic=ShorterRobotHeuristic, k=k)
    # test_robot(WAStartRobot, [3, 4], heuristic=center_manhattan_heuristic)
    # test_robot(WAStartRobot, [0, 1, 2, 3, 4, 5], heuristic=center_manhattan_heuristic)
    # for k in [2, 4, 6, 8]:
    #     test_robot(WAStartRobot, [0, 1, 2, 3, 4, 5], heuristic=ShorterRobotHeuristic, k=k)
    # for i in range(2,6):
    #     shorter_robot_heuristic_experiment(i)

    # a = solve_and_display(WAStartRobot, 50, heuristic=center_manhattan_heuristic, w=0.5, blit=False)
    # b = solve_and_display(WAStartRobot, 50, heuristic=ShorterRobotHeuristic, k=2, blit=False)
    # a = solve_and_display(WAStartRobot, 95, heuristic=center_manhattan_heuristic, w=0.5, blit=False)
    # b = solve_and_display(WAStartRobot, 95, heuristic=ShorterRobotHeuristic, k=2, blit=False)
    # w_experiment(50)
    # shorter_robot_heuristic_experiment(50)

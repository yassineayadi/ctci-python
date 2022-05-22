from chapter08.p02 import get_path


def test_robot_grid():
    grid = [
        [True, True, False, True],
        [True, True, False, True],
        [True, False, False, True],
        [True, True, True, True],
        [True, True, False, True],
    ]
    path = get_path(grid)
    print(path)

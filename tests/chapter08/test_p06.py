from chapter08.p06 import TowerOfHanoi


def test_tower_of_hanoi():

    tower_of_hanoi = TowerOfHanoi()
    print(tower_of_hanoi.multi_stack)
    tower_of_hanoi.solve(0, 2, 1)
    print(tower_of_hanoi.multi_stack)

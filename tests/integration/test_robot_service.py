import pytest
from unittest import TestCase
from domain.domain_entities import robot_mower
from domain.data_classes import coordinates
from domain.data_classes import instructions
from domain.domain_entities import area_flat_rectangular
from service_layer import services

class TestRobotService(TestCase):
    def setUp(self):
        self.area = area_flat_rectangular.AreaFlatRectangular(bottom_left=(0, 0), upper_right=(5, 5))
        self.robot_mower_01 = robot_mower.RobotMower(coordinates.Coordinates(1, 2), 'N')
        self.robot_mower_02 = robot_mower.RobotMower(coordinates.Coordinates(6, 2), 'E')
        self.robot_mower_01.deploy(self.area)
        self.robot_mower_02.deploy(self.area)

    def test_robot_can_move_north(self):
        self.robot_mower_01.move()
        assert self.robot_mower_01.position == coordinates.Coordinates(1, 3)

    def test_robot_can_receive_instructions(self):
        services.send_instructions(self.robot_mower_01, instructions.Instruction('RMM'))
        assert self.robot_mower_01.position == coordinates.Coordinates(3,3)

    def test_robot_can_move_east(self):
        pass

    def test_robot_can_move_west(self):
        pass

    def test_robot_can_move_south(self):
        pass

    def test_robot_can_rotate_left(self):
        pass

    def test_robot_can_rotate_right(self):
        pass

    def test_robot_remain_inside_the_area(self):
        pass

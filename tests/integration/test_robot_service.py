import pytest
from unittest import TestCase
from domain.domain_entities import robot_mower
from domain.data_classes import coordinates as c
from domain.domain_entities import area_flat_rectangular as a
from service_layer import services

class TestRobotService(TestCase):
    def setUp(self):
        self.area = a.AreaFlatRectangular(bottom_left=(0, 0), upper_right=(5, 5))
        self.robot_mower_01 = robot_mower.RobotMower()
        self.robot_mower_02 = robot_mower.RobotMower()
        self.robot_mower_01.deploy(c.Coordinates(1, 2), 'N', self.area)
        self.robot_mower_02.deploy(c.Coordinates(6, 2), 'E', self.area)

    def test_robot_can_move_north(self):
        self.robot_mower_01.move(self.area)
        assert self.robot_mower_01.position == c.Coordinates(1, 3)

    def test_robot_can_rotate_right(self):
        self.robot_mower_01.turn('R')
        assert self.robot_mower_01.position == c.Coordinates(1, 2)
        assert self.robot_mower_01.orientation == 'E'

    def test_robot_can_move_east(self):
        self.robot_mower_01.turn('R')
        self.robot_mower_01.move(self.area)
        assert self.robot_mower_01.position == c.Coordinates(2, 2)

    def test_robot_can_rotate_left(self):
        self.robot_mower_01.turn('L')
        assert self.robot_mower_01.position == c.Coordinates(1, 2)
        assert self.robot_mower_01.orientation == 'W'

    def test_robot_can_move_west(self):
        self.robot_mower_01.turn('L')
        self.robot_mower_01.move(self.area)
        assert self.robot_mower_01.position == c.Coordinates(0, 2)
        assert self.robot_mower_01.orientation == 'W'


    def test_robot_can_move_south(self):
        self.robot_mower_01.turn('L')
        self.robot_mower_01.turn('L')
        self.robot_mower_01.move(self.area)
        assert self.robot_mower_01.position == c.Coordinates(1, 1)
        assert self.robot_mower_01.orientation == 'S'

    def test_robot_can_receive_instructions(self):
        self.robot_mower_01.process_instructions('RMM')
        assert self.robot_mower_01.position == c.Coordinates(3, 2)
        assert self.robot_mower_01.orientation == 'E'

    def test_robot_remain_inside_the_area(self):
        pass
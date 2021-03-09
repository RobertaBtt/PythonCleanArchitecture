import pytest
from unittest import TestCase
from domain.domain_entities import robot_mower
from domain.data_classes import coordinates
from domain.domain_entities import area_flat_rectangular


class TestRobot(TestCase):

    def setUp(self):
        self.area = area_flat_rectangular.AreaFlatRectangular(bottom_left=(0, 0), upper_right=(5, 5))
        self.robot_mower_01 = robot_mower.RobotMower(coordinates.Coordinates(1, 2), 'N')
        self.robot_mower_02 = robot_mower.RobotMower(coordinates.Coordinates(6, 2), 'E')

    def test_check_robot_position(self):
        assert self.robot_mower_01.position == coordinates.Coordinates(1, 2)

    def test_robot_can_be_deployed(self):
        assert self.robot_mower_01.deploy(self.area)

    def test_robot_cannot_be_deployed(self):
        assert not self.robot_mower_02.deploy(self.area)

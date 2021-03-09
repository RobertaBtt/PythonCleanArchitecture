import pytest
from unittest import TestCase
from domain.domain_entities import robot_mower
from domain.data_classes import coordinates as c
from domain.domain_entities import area_flat_rectangular as a

class TestRobot(TestCase):

    def setUp(self):
        self.area = a.AreaFlatRectangular(bottom_left=(0, 0), upper_right=(5, 5))
        self.robot_mower_01 = robot_mower.RobotMower()
        self.robot_mower_02 = robot_mower.RobotMower()
        self.robot_mower_03 = robot_mower.RobotMower()

    def test_robot_can_be_deployed(self):
        assert self.robot_mower_01.deploy(c.Coordinates(1, 2), 'N', self.area)

    def test_robot_cannot_be_deployed_outside_area(self):
        assert not self.robot_mower_02.deploy(c.Coordinates(6,2), 'E', self.area)

    def test_robot_cannot_be_deployed_wrong_orientation(self):
        assert not self.robot_mower_03.deploy(c.Coordinates(2, 4), 'Z', self.area)

    def test_check_robot_position(self):
        self.robot_mower_01.deploy(c.Coordinates(1, 2), 'N', self.area)
        assert self.robot_mower_01.position == c.Coordinates(1, 2)

    def test_check_robot_orientation(self):
        self.robot_mower_01.deploy(c.Coordinates(1, 2), 'N', self.area)
        assert self.robot_mower_01.orientation == 'N'

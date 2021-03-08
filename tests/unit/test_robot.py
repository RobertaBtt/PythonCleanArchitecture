import pytest
from unittest import TestCase
from domain.domain_entities import robot_mower
from domain.data_classes import coordinates
from domain.domain_entities import area_flat_rectangular

class TestRobot(TestCase):

    def setUp(self):
        self.area = area_flat_rectangular.AreaFlatRectangular(bottom_left=(0,0),upper_right=(5,5))
        self.robot_mower_01 = robot_mower.RobotMower(coordinates.Coordinates(1,2))
        self.robot_mower_02 = robot_mower.RobotMower(coordinates.Coordinates(6,2))

    def test_check_identity_value_object(self):
        assert self.robot_mower_01.position == coordinates.Coordinates(1,2)

    def test_robot_can_be_deployed(self):
        assert self.robot_mower_01.deploy(self.area)

    def test_robot_cannot_be_deployed(self):
        assert not self.robot_mower_02.deploy(self.area)

    def test_two_robots_can_be_deployed(self):
        pass


    def test_robot_has_a_position(self):
        pass

    def test_robot_can_send_its_position(self):
        pass

    def test_robot_remain_inside_the_area(self):
        pass

    def test_robot_can_move_north(self):
        pass

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



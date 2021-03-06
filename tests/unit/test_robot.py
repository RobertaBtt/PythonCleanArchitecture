from unittest import TestCase
from domain.domain_entities import robot_mower
from domain.data_classes import coordinates as c
from domain.domain_entities import area_flat_rectangular as a

class TestRobot(TestCase):

    def setUp(self):
        self.area = a.AreaFlatRectangular()
        self.area.deploy(x_bottom=0, y_bottom=0, x_upper=5, y_upper=5)
        self.robot_mower_01 = robot_mower.RobotMower()
        self.robot_mower_02 = robot_mower.RobotMower()
        self.robot_mower_03 = robot_mower.RobotMower()

    def test_robot_can_be_deployed(self):
        assert self.robot_mower_01.deploy(x=1, y=2, orientation = 'N', area=self.area)

    def test_robot_cannot_be_deployed_outside_area(self):
        assert not self.robot_mower_02.deploy(x=6, y=2, orientation='E', area=self.area)

    def test_robot_cannot_be_deployed_wrong_orientation(self):
        assert not self.robot_mower_03.deploy(x=2, y=4, orientation='Z', area=self.area)

    def test_check_robot_position(self):
        self.robot_mower_01.deploy(x=1, y=2, orientation='N', area=self.area)
        assert self.robot_mower_01.position == c.Coordinates(1, 2)

    def test_check_robot_orientation(self):
        self.robot_mower_01.deploy(x=1, y=2, orientation='N', area=self.area)
        assert self.robot_mower_01.orientation == 'N'

    def test_robot_can_move_north(self):
        self.robot_mower_01.deploy(x=1, y=2, orientation='N', area=self.area)
        self.robot_mower_01.move(self.area)
        assert self.robot_mower_01.position == c.Coordinates(1, 3)

    def test_robot_can_rotate_right(self):
        self.robot_mower_01.deploy(x=1, y=2, orientation='N', area=self.area)
        self.robot_mower_01.turn('R')
        assert self.robot_mower_01.position == c.Coordinates(1, 2)
        assert self.robot_mower_01.orientation == 'E'

    def test_robot_can_move_east(self):
        self.robot_mower_01.deploy(x=1, y=2, orientation='N', area=self.area)
        self.robot_mower_01.turn('R')
        self.robot_mower_01.move(self.area)
        assert self.robot_mower_01.position == c.Coordinates(2, 2)

    def test_robot_can_rotate_left(self):
        self.robot_mower_01.deploy(x=1, y=2, orientation='N', area=self.area)
        self.robot_mower_01.turn('L')
        assert self.robot_mower_01.position == c.Coordinates(1, 2)
        assert self.robot_mower_01.orientation == 'W'

    def test_robot_can_move_west(self):
        self.robot_mower_01.deploy(x=1, y=2, orientation='N', area=self.area)
        self.robot_mower_01.turn('L')
        self.robot_mower_01.move(self.area)
        assert self.robot_mower_01.position == c.Coordinates(0, 2)
        assert self.robot_mower_01.orientation == 'W'

    def test_robot_can_move_south(self):
        self.robot_mower_01.deploy(x=1, y=2, orientation='N', area=self.area)
        self.robot_mower_01.turn('L')
        self.robot_mower_01.turn('L')
        self.robot_mower_01.move(self.area)
        assert self.robot_mower_01.position == c.Coordinates(1, 1)
        assert self.robot_mower_01.orientation == 'S'


from unittest import TestCase
from domain.domain_entities import robot_mower
from domain.data_classes import coordinates as c
from domain.domain_entities import area_flat_rectangular as a
from domain.domain_entities.robot_mower import RobotMower
from service_layer import services


class TestRobotService(TestCase):

    def setUp(self):
        self.area = a.AreaFlatRectangular()
        self.area.deploy(c.Coordinates(0, 0), c.Coordinates(5, 5))
        self.robot_mower_01 = robot_mower.RobotMower()
        self.robot_mower_01.deploy(c.Coordinates(1, 2), 'N', self.area)
        self.robot_mower_02 = robot_mower.RobotMower()
        self.robot_mower_02.deploy(c.Coordinates(3,3), 'E', self.area)
        self.robot_mower_03 = robot_mower.RobotMower()
        self.robot_mower_03.deploy(c.Coordinates(0,0), 'N', self.area)

    def test_create_area(self):
        x1 = 0
        y1 = 0
        x2 = 5
        y2 = 5

        area = services.create_area(x1, y1, x2, y2)
        assert area is not None
        assert isinstance(area, a.AreaFlatRectangular)

    def test_create_robot(self):
        x = 1
        y = 2
        orientation = 'N'
        this_robot_mower: RobotMower = services.create_robot(x, y, orientation, self.area)
        assert this_robot_mower is not None
        assert isinstance(this_robot_mower, RobotMower)
        assert this_robot_mower.orientation == 'N'

    def test_robot01_can_receive_instructions(self):
        services.send_instructions(self.robot_mower_01, 'LMLMLMLMM')
        assert self.robot_mower_01.position == c.Coordinates(1,3)
        assert self.robot_mower_01.orientation == 'N'

    def test_robot02_can_receive_instructions(self):
        services.send_instructions(self.robot_mower_02, 'MMRMMRMRRM')
        assert self.robot_mower_02.position == c.Coordinates(5,1)
        assert self.robot_mower_02.orientation == 'E'

    def test_robot03_remain_inside_the_area(self):
        services.send_instructions(self.robot_mower_03, 'MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM')
        assert self.robot_mower_03.position == c.Coordinates(0,5)
        assert self.robot_mower_03.orientation == 'N'

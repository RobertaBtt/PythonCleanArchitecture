from unittest import TestCase
from domain.domain_entities import area_flat_rectangular as a
from domain.data_classes import coordinates as c

class TestArea(TestCase):

    def setUp(self):
        self.area = a.AreaFlatRectangular()

    def test_an_area_can_be_deploy(self):
        assert self.area.deploy(c.Coordinates(0, 0), c.Coordinates(5, 5))
        assert self.area.bottom_left == c.Coordinates(0, 0)
        assert self.area.upper_right == c.Coordinates(5, 5)

    def test_an_area_cannot_be_deploy_negative_upper_right(self):
        area = a.AreaFlatRectangular()
        assert not area.deploy(c.Coordinates(0, 0), c.Coordinates(-1, 0))

    def test_an_area_cannot_be_deploy_negative_bottom_left(self):
        assert not self.area.deploy(c.Coordinates(-9, -1), c.Coordinates(90, 1))

    def test_an_area_cannot_be_deploy_zero_upper_right(self):
        assert not self.area.deploy(c.Coordinates(0, 0), c.Coordinates(0, 0))

    def test_point_is_inside(self):
        self.area.deploy(c.Coordinates(0, 0), c.Coordinates(5, 5))
        assert self.area.point_is_inside(x=0, y=0)
        assert self.area.point_is_inside(x=1, y=5)
        assert self.area.point_is_inside(x=5, y=5)
        assert not self.area.point_is_inside(x=6, y=5)
from unittest import TestCase
from domain.domain_entities import area_flat_rectangular

class TestArea(TestCase):

    def test_an_area_can_be_set(self):
        area = area_flat_rectangular.AreaFlatRectangular(bottom_left=(0,0),upper_right=(5,5))
        assert area.bottom_left == (0,0)
        assert area.upper_right == (5,5)
        assert area.is_coherent

    def test_an_area_cannot_be_set_negative_upper_right(self):
        area = area_flat_rectangular.AreaFlatRectangular(bottom_left=(0,0),upper_right=(-1,0))
        assert not area.is_coherent


    def test_an_area_cannot_be_set_negative_bottom_left(self):
        area = area_flat_rectangular.AreaFlatRectangular(bottom_left=(-9,-1),upper_right=(90,1))
        assert not area.is_coherent

    def test_an_area_cannot_be_set_zero_upper_right(self):
        area = area_flat_rectangular.AreaFlatRectangular(bottom_left=(0,0),upper_right=(0,0))
        assert not area.is_coherent
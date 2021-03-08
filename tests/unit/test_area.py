import pytest
from unittest import TestCase
from domain.domain_entities import robot_mower
from domain.data_classes import coordinates
from domain.domain_entities import area_flat_rectangular

class TestArea(TestCase):

    def test_an_area_can_be_set(self):
        area = area_flat_rectangular.AreaFlatRectangular(bottom_left=(0,0),upper_right=(5,5))
        assert area.bottom_left == (0,0)
        assert area.upper_right == (5,5)


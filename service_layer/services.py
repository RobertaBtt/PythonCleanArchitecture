from domain.data_classes import coordinates as c

from domain.domain_entities import area_flat_rectangular as flat_area
from domain.domain_entities import area as area_abstract

from domain.domain_entities import robot_mower as mower
from domain.domain_entities import robot


def create_area(bottom_x: int, bottom_y: int, upper_x: int, upper_y: int):
    area = flat_area.AreaFlatRectangular()
    if area.deploy(c.Coordinates(bottom_x, bottom_y), c.Coordinates(upper_x, upper_y)):
        return area


def create_robot(x: int, y: int, orientation_: str, area_: area_abstract) -> robot:
    robot_mower = mower.RobotMower()
    if robot_mower.deploy(c.Coordinates(x, y), orientation_, area_):
        return robot_mower
    else:
        return None


def send_instructions(robot_: robot, instructions: str):
    robot_.process_instructions(instructions)

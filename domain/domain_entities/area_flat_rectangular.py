from . import area
from domain.data_classes import coordinates as c

# An Area is an Entity because  it has a long-lived identity
# It will be always in the same coordinates/position
# and could have a name/identification.


class AreaFlatRectangular(area.Area):

    def deploy(self, coordinates_bottom: c.Coordinates, coordinates_upper: c.Coordinates):
        if coordinates_bottom == c.Coordinates(0, 0) and coordinates_upper.x > 0 and coordinates_upper.y > 0:
            self.bottom_left = coordinates_bottom
            self.upper_right = coordinates_upper
            return True
        return False

    def point_is_inside(self, **kwargs):
        if self.upper_right.x >= kwargs['x'] >= self.bottom_left.x and self.upper_right.y >= kwargs['y'] >= self.bottom_left.y:
            return True
        return False



from . import area
from domain.data_classes import coordinates as c

# An Area is an Entity because  it has a long-lived identity
# It will be always in the same coordinates/position
# and could have a name/identification.


class AreaFlatRectangular(area.Area):

    def deploy(self, **kwargs):
        if kwargs['x_bottom'] == 0 and kwargs['y_bottom'] == 0 and kwargs['x_upper'] >0 and kwargs['y_upper'] > 0:
            self.bottom_left = c.Coordinates(kwargs['x_bottom'], kwargs['y_bottom'])
            self.upper_right = c.Coordinates(kwargs['x_upper'], kwargs['y_upper'])
            return True
        return False

    def point_is_inside(self, **kwargs):
        if self.upper_right.x >= kwargs['x'] >= self.bottom_left.x and self.upper_right.y >= kwargs['y'] >= self.bottom_left.y:
            return True
        return False



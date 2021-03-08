from . import area
# An Area is an Entity because  it has a long-lived identity
# It will be always in the same coordinates/position
# and could have a name/identificator.

class AreaFlatRectangular(area.Area):

    def __init__(self, **kwargs):
        self._bottom_left = None
        self._upper_right = None
        if self.__check_integrity__(**kwargs):
            self._bottom_left = kwargs['bottom_left']
            self._upper_right = kwargs['upper_right']

    def __check_integrity__(self, **kwargs):
        bottom_left = kwargs['bottom_left']
        upper_right = kwargs['upper_right']
        if bottom_left == (0,0) and upper_right[0]>0 and upper_right[1]>0:
            return True
        return False

    def point_is_inside(self, **kwargs):
        return True


    @property
    def bottom_left(self):
        return self._bottom_left

    @property
    def upper_right(self):
        return self._upper_right


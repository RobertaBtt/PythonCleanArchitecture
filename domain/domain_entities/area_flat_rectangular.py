from . import area

class AreaFlatRectangular(area.Area):

    def __init__(self, **kwargs):
        if self.__check_integrity__(**kwargs):
            self._bottom_left = kwargs['bottom_left']
            self._upper_right = kwargs['upper_right']

    def __check_integrity__(self, **kwargs):
        return True

    def point_is_inside(self, **kwargs):
        return True


    @property
    def bottom_left(self):
        return self._bottom_left

    @property
    def upper_right(self):
        return self._upper_right


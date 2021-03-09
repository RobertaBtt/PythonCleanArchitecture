from dataclasses import dataclass

ORIENTATIONS = ['N', 'S', 'E', 'W']


@dataclass
class Orientation:
    orientation: str

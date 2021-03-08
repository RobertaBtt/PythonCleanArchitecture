from dataclasses import dataclass
from dataclasses import field

@dataclass
class Instruction:
    instruction_list: list[str] = field(default_factory=list)

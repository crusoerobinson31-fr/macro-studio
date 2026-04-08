from dataclasses import dataclass
from typing import List
import time

@dataclass
class MacroStep:
    action: str
    value: str = ""
    delay: float = 0.1

class Macro:
    def __init__(self):
        self.steps: List[MacroStep] = []

    def add_step(self, action: str, value: str = "", delay: float = 0.1):
        self.steps.append(MacroStep(action, value, delay))

import time
from macro_app.macro_engine import Macro

class MacroPlayer:
    def __init__(self, logger=print):
        self.logger = logger
        self.running = False

    def play(self, macro: Macro):
        self.running = True
        self.logger("▶ Lecture macro")

        for step in macro.steps:
            if not self.running:
                self.logger("⏹ Lecture arrêtée")
                return

            self.logger(f"Action: {step.action} {step.value}")
            time.sleep(step.delay)

        self.logger("✅ Macro terminée")

    def stop(self):
        self.running = False
``

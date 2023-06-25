import pytest
import os
import re
from logger import CoffeeMachine

dir_path = os.path.dirname(os.path.realpath(__file__))

def test_coffee_machine():
    machine = CoffeeMachine()
    for i in range(0, 5):
        machine.make_coffee()
    machine.make_coffee()
    machine.add_water(70)

    with open("machine.log", "r") as log_file, open(os.path.join(dir_path, "machine.log.correct"), "r") as correct_file:
        for log_line, correct_line in zip(log_file, correct_file):
            log_line = re.sub(r"\[ exec-time = .* \]", "", log_line)
            correct_line = re.sub(r"\[ exec-time = .* \]", "", correct_line)
            assert log_line == correct_line

    os.remove("machine.log")

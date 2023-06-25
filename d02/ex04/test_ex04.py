from my_minipack import progress, log
from random import randint
import pytest
import time

class CoffeeMachine():
    water_level = 100

    @log
    def make_coffee(self):
        self.water_level = 90
        print("Coffee is ready!")

class TestMyMinipack:

    def test_progress(self):
        for i in progress(range(100)):
            pass
        assert i == 99, "ft_progress function failed"

    def test_log(self):
        machine = CoffeeMachine()
        machine.make_coffee()
        assert machine.water_level == 90, "log function failed"

if __name__ == "__main__":
    pytest.main()

import pytest
import numpy as np
from TinyStatistician import TinyStatistician

@pytest.fixture
def tstat():
    return TinyStatistician()

def test_mean(tstat):
    data = [np.random.rand(50) for _ in range(10)]
    for d in data:
        assert np.isclose(tstat.mean(d), np.mean(d))

def test_median(tstat):
    data = [np.random.rand(50) for _ in range(10)]
    for d in data:
        assert np.isclose(tstat.median(d), np.median(d))

def test_quartiles(tstat):
    data = [np.random.rand(50) for _ in range(10)]
    for d in data:
        q1, q3 = tstat.quartile(d)
        assert np.isclose(q1, np.percentile(d, 25), atol=0.1)
        assert np.isclose(q3, np.percentile(d, 75), atol=0.1)

def test_var(tstat):
    data = [np.random.rand(50) for _ in range(10)]
    for d in data:
        assert np.isclose(tstat.var(d), np.var(d))

def test_std(tstat):
    data = [np.random.rand(50) for _ in range(10)]
    for d in data:
        assert np.isclose(tstat.std(d), np.std(d))

import pytest


def test_numpy() -> None:
    try:
        import numpy as np

        np.zeros(0)
    except ImportError:
        pytest.fail("Numpy is not available")


def test_pandas() -> None:
    try:
        import pandas as pd

        pd.DataFrame()
    except ImportError:
        pytest.fail("Pandas is not available")


def test_scikit_learn() -> None:
    try:
        import sklearn as skl

        skl.show_versions()
    except ImportError:
        pytest.fail("Sci-Kit Learn is not available")


def test_matplotlib() -> None:
    try:
        import matplotlib

        matplotlib.__name__
    except ImportError:
        pytest.fail("Matplotlib is not available")

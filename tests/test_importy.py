import importlib

import pytest


@pytest.mark.parametrize("numer", range(1, 7))
def test_pakiet_zestawu_sie_importuje(numer):
    importlib.import_module(f"zestaw_{numer}")

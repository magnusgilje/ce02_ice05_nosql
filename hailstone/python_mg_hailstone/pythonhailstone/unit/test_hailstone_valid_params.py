import sys
import pytest
sys.path.insert(0,"..")
import hailstone

def test_hailstone_valid_params():
    myH = hailstone.Hailstone(4)
    assert myH.plot() == [4,2,1]
    # assert myH.steps() ==     
    # assert myC.summary() == 'area=3.14, perimeter=6.28'

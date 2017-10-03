# -*- coding: utf-8 -*-
"""
Created on Tue Oct 03 09:29:32 2017

@author: cavasinf
"""

import S1_algotools as algo, pytest

#========== ZONE DE TESTS ============
def test_average_above_zero():
    assert algo.average_above_zero([1,3,9,4,-7]) == 4.25
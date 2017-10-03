# -*- coding: utf-8 -*-
"""
Created on Tue Oct 03 09:29:32 2017

@author: cavasinf
"""

import S1_algotools as algo, pytest
input_list=[1,0,3,9,4,-7]

#========== ZONE DE TESTS ============
def test_average_above_zero():
    assert algo.average_above_zero(input_list) == 4.25
    
def test_max_value():
    assert algo.max_value(input_list) == 9
    
def test_reverse_table():
    assert algo.reverse_table(input_list) == [-7, 4, 9, 3, 0, 1]
    
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 17:01:31 2022

@author: zzw
"""
import simple_math

def test_simple_add():
 assert simple_math.simple_add(5,10) == 15
 
def test_simple_sub():
 assert simple_math.simple_sub(5,10) == -5
 
def test_simple_mult():
 assert simple_math.simple_mult(5,10) == 50
 
def test_simple_div():
 assert simple_math.simple_div(5,10) == 0.5

def test_poly_first():
 assert simple_math.poly_first(5, 10, 5) == 35
 
def test_poly_second():
 assert simple_math.poly_second(5, 10, 15, 10) == 335
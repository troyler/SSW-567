# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation
@author: jrr
@author: rk
"""
import unittest
from Triangle import classifyTriangle
# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework
class TestTriangles(unittest.TestCase):
    "define multiple sets of tests as functions with names that begin"

    def test_right_triangle_a(self):
        "try a standard right triangle"
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')
    def test_right_triangle_b(self):
        "try a standard right triangle, testing for order"
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')

    def test_equilateral_triangles(self):
        "try a standard equilateral triangle"
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def test_valid_triangle(self):
        "test against an invalid triangle"
        self.assertEqual(classifyTriangle(100,1,101),'NotATriangle','100,1,501 is not a triangle')

    def test_outside_range(self):
        "test against an invalid triangle due to requirements < 200"
        self.assertEqual(classifyTriangle(250,300,60),'InvalidInput')

    def test_against_negative(self):
        "test against negative inputs"
        self.assertEqual(classifyTriangle(-1,300,60),'InvalidInput')

    def test_scalene(self):
        "test against a scalene triangle"
        self.assertEqual(classifyTriangle(12,30,20),'Scalene','12,30,20 is a Scalene triangle')

    def test_isosceles(self):
        "test against an isosceles triangle"
        self.assertEqual(classifyTriangle(12,15,12),'Isosceles','12,15,12 is an Isosclees Triangle')

    def test_bad_input(self):
        "test against ivalid argument types"
        self.assertEqual(classifyTriangle("12", "15", "20"),'InvalidInput','Input should be integers')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
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
    # define multiple sets of tests as functions with names that begin
    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')
    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')

    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')
        
    def testValidTriangle(self): 
        self.assertEqual(classifyTriangle(100,1,101),'NotATriangle','500,1,502 is not a triangle')

    def testScalene(self): 
        self.assertEqual(classifyTriangle(12,30,20),'Scalene','12,30,20 should be a Scalene triangle')

    def testIsosceles(self): 
        self.assertEqual(classifyTriangle(12,15,12),'Isosceles','12,15,12 should be an Isosclees Triangle')
    
    def testBadInput(self): 
        self.assertEqual(classifyTriangle("12", "15", "20"),'InvalidInput','Input should be integers')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
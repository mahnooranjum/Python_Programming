# -*- coding: utf-8 -*-


import unittest 
import calc

class TestCalc(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print('setup Class')
        
    @classmethod
    def tearDownClass(cls):
        print('Tear Class')
        
    def setUp(self):
        print('Setup')
        pass
    
    def tearDown(self):
        print('Tear')
        pass
    
    def test_add(self):
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(-1, -2), -3)    
        
    def test_sub(self):
        self.assertEqual(calc.sub(10, 5), 5)
        self.assertEqual(calc.sub(-1, 1), -2)
        self.assertEqual(calc.sub(-1, -2), 1)    
        
    def test_mul(self):
        self.assertEqual(calc.mul(10, 5), 50)
        self.assertEqual(calc.mul(-1, 1), -1)
        self.assertEqual(calc.mul(-1, -2), 2)    
        
    def test_div(self):
        self.assertEqual(calc.div(10, 5), 2)
        self.assertEqual(calc.div(-1, 1), -1)
        self.assertEqual(calc.div(-1, -2), 0.5)    
        # self.assertRaises(ValueError,calc.div, 10, 0)
        with self.assertRaises(ValueError):
            calc.div(10,0)
 
if __name__ == '__main__':
    unittest.main()
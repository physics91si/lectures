import sets 
import unittest

class TestSetMethods(unittest.TestCase):
    
    def setUp(self):
        self.A = sets.Set([1,2,3])
        self.B = sets.Set([3,4,5])
    
    def test_or(self):
        C = self.A | self.B
        self.assertEqual(C.data, [1,2,3,4,5] , 'wrong union')
        
    def test_and(self):
        D = self.A & self.B
        self.assertEqual(D.data, [3] , 'wrong intersection')
    
    def test_sub(self):
        E = self.A - self.B
        self.assertEqual(E.data, [1,2] , 'wrong difference')

if __name__ == '__main__':
    unittest.main()


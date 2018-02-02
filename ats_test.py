''' Test valrious methods in Ball and Platform class
Project
Created on Jul 30, 2015

@author: frankboye
'''

import unittest
from ball import *
from platform import *


class Test(unittest.TestCase):
    '''class to test methods in platform and ball classes
    Sidenote: Methods that are not here but are in the class were excluded
                because the application is evidence that they work.
    '''

    def testBallConstructor(self):
        '''test Ball constructor
        '''
        try:
            #create ball object for testing and assert constructor variables
            ball = Ball(30,40,10,'blue')
            assert ball._x == 30
            assert ball._y == 40
            assert ball._radius == 10
            assert ball._color == 'blue'
        #these assertions should not fail
        except:
            self.fail('This should not raise an exception')
            
    def testBadConstructorException(self):
        '''test bad constructor and excpetion
        '''
        try:
            #test bad exception radius should only be 14 because I dont want a big ball 
            ball = Ball(50,70,14,'yellow')
            ball._radius == 14
            self.fail('This should raise an exception')
        except:
            pass
    
    def testGetx_GetY_GetVelx_GetVelY_GetRadius(self):
        '''test accessor methods'''
        try:
            #create ball object for testing and assert various get methods
            ball = Ball(30,40,10,'blue')
            assert ball.get_x() == 30
            assert ball.get_y() == 40
            assert ball.get_radius() == 10
            assert ball.get_velx() == 15
            assert ball.get_vely() == 15
            #these assertions should not fail
        except:
            self.fail('This should not raise an exception')
            
    def test_in_on_platform(self):
        '''test if ball is on a platform'''
        try:
            #create an empty list and append different platforms to it
            p_list = []
            p = Platform(10, 530, 110)
            p_list.append(p)
            p1 = Platform(170, 570, 110,'red',10)
            p_list.append(p1)
            #create a ball object that should be on these platforms
            ball = Ball(30,519,10)
            #assert that the ball is on the platform
            assert ball.is_on_platform(p_list) == p
        #test should not fail
        except:
            self.fail('This should not raise an exception')
      
    def testPlatformConstructor(self):
        try:
            #create platform objects o test
            p = Platform(10, 530, 110)
            p1 = Platform(60, 330, 260, 'blue', 5)
            #assert platfomrs constructor
            assert p._x == 10
            assert p._y == 530
            assert p._length == 110
            assert p._color == 'red'
            assert p._velx == 0
            #assert second plaforms constructor
            assert p1._x == 60
            assert p1._y == 330
            assert p1._length == 260
            assert p1._color == 'blue'
            assert p1._velx == 5
        #It should notn fail the test
        except:
            self.fail('This should not raise an exception')

    def test_GetX1_GetX2_Get_Y1_GetVelX_Get_height(self):
        '''test accessor methods of platform class'''
        try:
            #test for first platform
            p = Platform(10, 530, 110)
            assert p.get_x1() == 10
            assert p.get_x2() == 10 + 110
            assert p.get_velx() == 0
            assert p.get_y1() == 530
            #test for second platform
            p1 = Platform(300, 50, 25,'red', 30)
            assert p1.get_x1() == 300
            assert p1.get_x2() == 300 + 25
            assert p1.get_velx() == 30
            assert p1.get_y1() == 50
            #it should not fail the test
        except:
            self.fail('This should not raise an exception')
            


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
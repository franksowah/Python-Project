'''Class to create a ball to use in our game
Project
Created Summer 2015
@author: Emmanuel Boye (efb4)
'''
from my_platform import *
class Ball:
    '''Class to build a ball
    '''
    
    def __init__(self, x, y, radius, color = 'yellow'):
        '''Ball class constructor
        '''
        
        self._x = x
        self._y = y
        self._velX = 15
        self._velY = 15
        self._radius = radius
        self._color = color
        
        #I dont want the ball to be too big or too small i want it to be of radius 10
        if self._radius != 10:
            raise ValueError('Radius should be only 10!')
        else:
            self._radius = radius
        
    def render(self, canvas):
        '''method that draws a circular representation of the particle to a canvas
        '''
        canvas.create_oval(self._x - self._radius,
                        self._y - self._radius,
                        self._x + self._radius,
                        self._y + self._radius,
                        fill = self._color)

    def get_x(self):
        '''get x cordinate of ball
        '''
        return self._x
    
    def get_y(self):
        '''get y coordinate of ball
        '''
        return self._y
    
    def get_radius(self):
        '''get radius of ball
        '''
        return self._radius
    
    def move_right(self, canvas):
        '''method to enable particle have movement
        '''
        #The move method should update the x and y coordinates of the 
        #particle according to their velocities (e.g. self._x += self._velX).
        self._x += self._velX
        
    def move_left(self, canvas):
        '''method to enable ball move left
        '''
        #The move method should update the x and y coordinates of the 
        #particle according to their velocities (e.g. self._x += self._velX).
        self._x += -self._velX
    
    def move_down(self, canvas):
        '''method to move ball down
        '''
        self._y += self._velY
        #if the ball reaches the bottom of the canvas ball should stop moving
        if (self._y + self._radius > canvas.winfo_reqwidth()) or self._y - self._radius < 0:
            self._velY = 0
    
    def jump(self,canvas):
        '''method that simulates a ball jumping
        this method works a bit well because the ball is supposed to automatically
        come down when its not on the platform
        '''
        #increase y by velocity and add an extra boost
        self._y += -self._velY - 65
        #increase x to give a somewhat circular motion
        self._x += self._velX + 40

   
    def get_vely(self):
        '''get y velocity of ball
        '''
        return self._velY  
    
    def get_velx(self):
        '''accessor for velocity x'''
        return self._velX 
        
    def is_on_platform(self, platform):
        '''method to ckeck if ball is on platform
        '''
        #receive a list and iterate through list
        for  i in  platform:
            # return platform if ball's x coordinate is inbetween the x coordinates of the platform and y cordinates of platform and top of ball
            if (i.get_x1() <= self._x <= i.get_x2()) and i.get_y1() <= self._y+ (self._radius*2) <= (i.get_y1() + (self._radius*2)):
                return i
        return None
    
    def move(self, canvas, plat):
        '''let ball move along with moving platform'''
        self._x += plat.get_velx()

 
if __name__ == '__main__':
    b = Ball(30,519,10)

#create empty list
    p_list = []
    
    #create Platform objects and append them to list
    p = Platform(10, 530, 110)
    p_list.append(p)
    
    p5 = Platform(350, 450,140)
    p_list.append(p5)
   
    #this platfroms moves
    p1 = Platform(170, 474, 110,'red', 2.5)
    p_list.append(p1)

    p4 = Platform(600, 530, 99)
    #append platoforms to list
    p_list.append(p4) 
    #test is on platform method it should return platform object location or None
    print(b.is_on_platform(p_list))
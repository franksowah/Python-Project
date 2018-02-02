'''Class to create platforms to use in the game
Created Summer 2015
Project
@author: Emmanuel Boye (efb4)
'''

class Platform:
    '''Class to create a platform
    default color of platform is red
    '''
    def __init__(self, x, y, length, color = 'red',  velocity = 0 ):
        '''platform constructor'''
        self._x = x
        self._y = y
        self._length = length
        self._color = color
        self._velx = velocity
        
    def render(self, canvas):
        '''method that draws a circular representation of the particle to a canvas
        '''
        #create rectangle on canvas
        canvas.create_rectangle (self._x,self._y, self._x + self._length,self._y + 15 , fill = self._color)
     
    def get_velx(self):
        return self._velx
       
    def get_x1(self):
        '''get first x coord of platform'''
        return self._x
    
    def get_x2(self):
        '''get second x coord of platform'''
        return self._x +self._length
    
    def get_y1(self):
        '''get y coord ot platform'''
        return self._y
    
    def plat_move(self, canvas, other):
        '''enable platform movement'''
        #if pltofmors gets tot the edge of the screen it should bounce back or if it gets to the edge of another platform
        #and it should move continuously
        self._x += self._velx
        if (self._x + self._length > canvas.winfo_reqwidth()) or self._x - self._length < 0 or self._x + self._length  > canvas.winfo_reqwidth() - other ._length or self._x + self._length  > canvas.winfo_reqwidth() + other ._length:
            self._velx = -self._velx
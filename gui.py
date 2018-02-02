'''Across The Sky game Graphical Interface
The Purpose of the game is to cross the screen without falling off the platforms
Created Summer 2015
Project
@author: Emmanuel Boye (efb4)
'''

from tkinter import *
from ball import *
from my_platform import *

class Gui:
    ''' Graphical User Interface class
    '''
    def __init__(self,window):
        '''Gui constructor
        '''
        #create a window to place widgets on
        self.window = window
        self.window.protocol('WM_DELETE_WINDOW', self.safe_exit)
        
        #set hieght nd width of screen and create canvas
        self.width = 700
        self.height = 700       
        self.canvas = Canvas(self.window,
                        width=self.width, height=self.height)
        
        #Photo widgets which are called when you win or lose the game
        self.photo = PhotoImage(file='cloud1.gif')
        self.photo1 = PhotoImage(file='images.gif')
        self.photo2 = PhotoImage(file= 'you_won.gif')
        self.photo3 = PhotoImage(file= 'explo.gif')

        self.canvas.pack()
        
        #create a quit game button
        quit_button = Button(window, text= 'Quit', command= self.safe_exit)
        quit_button.pack(side= RIGHT)
        
        #score accumulator which keeps track of the score in the game
        self.score = 0
        
        
        #bind movement functions to keys up, left, and right
        root.bind('<Right>', self.move_right)
        root.bind('<Left>', self.move_left)
        root.bind('<Up>', self.jump)

        #create empty list
        self.p_list = []
        
        #create Platform objects and append them to list
        p = Platform(10, 530, 110)
        self.p_list.append(p)
               
        #this platfroms will move
        p1 = Platform(170, 570, 110,'red',10)
        self.p_list.append(p1)

        p4 = Platform(600, 530, 99)
        self.p_list.append(p4)
#         
        #create ball object
        self.ball = Ball(30,519,10)
        
        self.terminated = False
        
        #forever loop to run game animation
        while self.terminated == False: 
            self.canvas.delete(ALL)
            #background image
            self.canvas.create_image(0, 0, image=self.photo, anchor=NW)
           #show score on canvas
            self.canvas.create_text(60,50, text='Score: ' + str(self.score), font=("Comic Sans", 25))
           #loop through platforms in the list and render them to canvas
            for platform in self.p_list:
                platform.render(self.canvas)
                #move the platforms that have a velocity
                platform.plat_move(self.canvas, platform)
                
            #if the ball is on the platform reder the ball to canvas else let the ball fall to its death
            if self.ball.is_on_platform(self.p_list):
                self.ball.render(self.canvas)    
            else:
                self.ball.render(self.canvas)
                self.ball.move_down(self.canvas)
            
            #let the ball move along with the platform    
            platform = self.ball.is_on_platform(self.p_list)
            if platform != None:
                self.ball.move(self.canvas, platform)
            else:
                self.ball.move_down(self.canvas)

             
                
                
            #if ball falls off platform to the bottom of screen call game over image and stop animation
            if self.ball.get_y() + self.ball.get_radius() > self.canvas.winfo_reqheight() :
                self.canvas.create_image(0, 0, image=self.photo1, anchor=NW)
                #add a picture that shows that ball has exploded
                self.canvas.create_image(self.ball.get_x()-25 , self.ball.get_y()-40, image=self.photo3, anchor=NW)
                self.terminated = not(self.terminated)
            
            #if you manage to make it to the end of the level you will be shown a picture saying 'You Win' and your score 
            if self.ball.get_x() + self.ball.get_radius() > self.canvas.winfo_reqwidth():
                self.canvas.create_image(0, 0, image=self.photo2, anchor=NW)
                self.canvas.create_text(100, 500, anchor=W, font=("Comic Sans MS", 25, 'bold'),
            text= 'You finished the level with a score of: ' + str(self.score))
                self.terminated = not(self.terminated)
            
            #show a message on screen for any particular score you get in this particulr level
                if 0<=self.score<=3:
                    self.canvas.create_text(300, 600, anchor=W, font=("Times", 19, 'bold'),
                text= 'You can do better')
                if 4<=self.score<=8:
                    self.canvas.create_text(300, 600, anchor=W, font=("Times", 19, 'bold'),
                text= 'You are getting there')
                if 9<=self.score<=13:
                    self.canvas.create_text(300, 600, anchor=W, font=("Times", 19, 'bold'),
                text= 'You did pretty well')

            self.canvas.after(50)
            self.canvas.update()
    
    
    def move_right(self, event):
        '''allows right movement
        '''
        #call the ball's move right method and increment score by one
        self.ball.move_right(self.canvas)
        self.score += 1

    
    def move_left(self, event):
        '''allows left movement
        '''
        #call the ball's move right method and decrease score by two
        self.ball.move_left(self.canvas)
        self.score -= 2
     
    def jump(self, event):
        '''allows ball to jump'''
        self.ball.jump(self.canvas)      
             
    def safe_exit(self):
        '''turn of event loop before closing the program'''
        self.terminated = True
        self.window.destroy()
        
        
if __name__ == '__main__':
    root =Tk()
    root.title('Across the Sky by efb4')    
    app = Gui(root)
    root.mainloop()

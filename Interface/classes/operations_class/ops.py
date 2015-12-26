'''
Created on Dec 6, 2015
contains the classes for the operation screen

@author: shaibujnr
'''
from kivy.uix.screenmanager import Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

class Operation_screen(Screen):
    pass
class Operation_grid(GridLayout):
    def __init__(self,*args,**kwargs):
        super(Operation_grid,self).__init__(**kwargs)
        self.button = Operation_button()
        self.height_increment = self.button.height
        self.texts = [
                      "Input Matrix","Determinant","Transpose",
                      "Matrix \nMultiplication","Scalar \nMultiplication",
                      "Addition","Subtraction","Cofactors","Inverse",
                      "Adjoint",
                      ]
        self.cols = 4
        if int(len(self.texts))%self.cols == 0:
            self.rows = int(len(self.texts))/self.cols
        else:
            self.rows = (int(len(self.texts))/self.cols)+1
        
        for i in range(int(len(self.texts))):
            self.add_widget(Operation_button(text=self.texts[i]))
        self.height = ((self.height_increment *self.rows)+(2*self.padding[0])+
                       (self.rows*self.spacing[0])+self.height_increment)
            
class Operation_button(Button):
    pass
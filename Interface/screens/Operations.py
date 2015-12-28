'''
Created on Dec 6, 2015
contains the classes for the operation screen

@author: shaibujnr
'''
from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout

Builder.load_string("""
<OperationButton>:
    size_hint: 1,None
    height: "100dp"
    
<OperationGrid>:
    spacing: "5dp"
    padding: "5dp"
    
<OperationScreen>:
    ScrollView:
        id: sv
        size_hint: None,None
        width: root.width
        height: root.height
        OperationGrid:
            size_hint: None,None
            width: root.width
            on_touch_down: print self.height,sv.height

""")
class OperationButton(Button):
    pass

class OperationGrid(GridLayout):
    def __init__(self,*args,**kwargs):
        super(OperationGrid,self).__init__(**kwargs)
        self.cols =  4
        self.size_hint = None,None
        self.ref_button = OperationButton()
        self.height = 0
        self.texts = [
                      "Input Matrix",
                      "Determinant",
                      "Adjoint",
                      "Inverse",
                      "Cofactors",
                      "Addition",
                      "Subtraction",
                      "Multiplication",
                      "Transpose",
                      "Scalar\nMultiplication"
                      ]
        if int(len(self.texts))%self.cols == 0:
            self.rows = int(len(self.texts))
        else:
            self.rows = int(len(self.texts))+1
        self.fill()
        self.height += self.padding[1]*2
        self.height += (self.spacing[1] * (self.rows-1))
        self.height += self.ref_button.height * self.rows
        
    def fill(self):
        for operations in self.texts:
            self.add_widget(
                            OperationButton(
                                            text=operations,
                                            
                                            )
                            )
            

class OperationScreen(Screen):
    pass
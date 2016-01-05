'''
Created on Dec 6, 2015
contains the classes for the operation screen

@author: shaibujnr
'''
from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty

from functools import partial

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
            cols: 4
            rows: 3
            height: ((self.rows*r_button.height)+(self.spacing[1]*(self.rows-1))+(self.padding[1]*2))
            width: root.width
            OperationButton:
                id: r_button
                text: "Input Matrix"
                on_press: root.sm.current = "input_matrix_screen"
            OperationButton:
                text: "Determinant"
                on_press: root.sm.current = "determinant_screen"
            OperationButton:
                text: "Inverse"
            OperationButton:
                text: "Addition"
            OperationButton:
                text: "Subtraction"
            OperationButton:
                text: "Multiplication"
            OperationButton:
                text: "Cofactors"
                on_press: root.sm.current = "cofactors_screen"
            OperationButton:
                text: "Adjoint"
                on_press: root.sm.current = "adjoint_screen"
            OperationButton:
                text: "Transpose"
                on_press: root.sm.current = "transpose_screen"
            OperationButton:
                text: "Scalar Multiplication"


""")
class OperationButton(Button):
    pass

class OperationGrid(GridLayout):
    def __init__(self,*args,**kwargs):
        super(OperationGrid,self).__init__(**kwargs)
        

class OperationScreen(Screen):
    """
    OperationButton instance needs access to the app root(screenmanager) in order
    to switch screens between operations. The 'sm' variable holds the screenmanager
    object allowing the button to call the screenmanager by 'root.sm' in the above 
    kv string.
    """
    sm = ObjectProperty() 
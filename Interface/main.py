'''
Created on Dec 5, 2015

@author: shaibujnr
'''
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.properties import ObjectProperty
from kivy.clock import Clock


from screens.Operations import OperationScreen
from screens.input_matrix import InputScreen
from screens.Determinant import DeterminantScreen
from screens.Adjoint import AdjointScreen
from screens.Cofactors import CofactorsScreen
from screens.Transpose import TransposeScreen









class root(ScreenManager):
    """
    *ScreenManager to manage transition between each screen
    *input_screen holds the InputScreen object defined in input_matrix.py
    """



class MatApp(App):
    def build(self):
        return root()
    
if __name__ == "__main__":
    MatApp().run()
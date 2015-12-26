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



from classes.operations_class.ops import *
from classes.input_matrix_class.input_matrix import *


Builder.load_file("screens/operations.kv") #load operations.kv for the operations screen
Builder.load_file("screens/input_matrix.kv")#load input_matrix.kv for the input screen





class root(ScreenManager):
    """
    *ScreenManager to manage transition between each screen
    *input_screen holds the InputScreen object defined in input_matrix.py
    """
    input_screen = ObjectProperty() 



class MatApp(App):
    def build(self):
        return root()
    
if __name__ == "__main__":
    MatApp().run()
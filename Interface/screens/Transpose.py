'''
Created on Jan 2, 2016

@author: shaibujnr
'''
from Interface.extra.customscreen import CustomScreen

class TransposeScreen(CustomScreen):
    def __init__(self,*args,**kwargs):
        super(TransposeScreen,self).__init__(**kwargs)
        self.op_button_text = "Transpose"
        self.type_button_text = "Square Matrix"
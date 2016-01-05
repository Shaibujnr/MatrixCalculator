'''
Created on Dec 27, 2015

@author: shaibujnr
'''

from Interface.extra.customscreen import CustomScreen

class AdjointScreen(CustomScreen):
    def __init__(self,*args,**kwargs):
        super(AdjointScreen,self).__init__(**kwargs)
        self.op_button_text = "Adjoint"
        self.type_button_text = "Square Matrix"



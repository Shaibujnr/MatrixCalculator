'''
Created on Jan 2, 2016

@author: shaibujnr
'''
from Interface.extra.customscreen import CustomScreen

class CofactorsScreen(CustomScreen):
    def __init__(self,*args,**kwargs):
        super(CofactorsScreen,self).__init__(**kwargs)
        self.op_button_text = "Cofactors"
        self.type_button_text = "Square Matrix"
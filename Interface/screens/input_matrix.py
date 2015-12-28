'''
Created on Dec 9, 2015

@author: shaibujnr

'''
from kivy.lang import Builder
from Interface.extra.customscreen import CustomScreen


from kivy.app import App

class InputScreen(CustomScreen):
    pass

class InputScreenApp(App):
    def build(self):
        return InputScreen()
    
if __name__ == "__main__":
    InputScreenApp().run()
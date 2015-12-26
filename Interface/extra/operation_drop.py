from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty,NumericProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.lang import Builder





class OperationButton(Button):
    def __init__(self,*args,**kwargs):
        super(OperationButton,self).__init__(**kwargs)
        self.size_hint_y = None
        
class OperationDrop(DropDown):
    button_height = NumericProperty(50)
    def __init__(self,*args,**kwargs):
        super(OperationDrop,self).__init__(**kwargs)
        self.dismiss_on_select = True
        self.auto_width = True
        self.buttons = [
                        "Determinant",
                        "Transpose",
                        "Inverse",
                        "Multiplication",
                        "Addition",
                        "Subtraction",
                        "Adjoint",
                        "Cofactors",
                        "Scalar Multiplication"
                        ]
        for tags in self.buttons:
            self.add_widget(OperationButton(text=tags,height=self.button_height))
            

class Root(Widget):
    def __init__(self,*args,**kwargs):
        super(Root,self).__init__(**kwargs)
        self.dropdown = OperationDrop()
        self.mainbutton = Button(text="hello",center=(200,400),size=(500,100))
        self.mainbutton.bind(on_release=self.dropdown.open)
        self.add_widget(self.mainbutton)

class testApp(App):
    def build(self):
        return Root()
    
if __name__ == "__main__":
    testApp().run()
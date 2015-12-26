'''
Created on Dec 9, 2015

@author: shaibujnr
'''

from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty,NumericProperty
from kivy.lang import Builder
from extra.operation_drop import OperationDrop
from extra.type_drop import TypeDrop






class FloatInput(TextInput):
    """
    intialising the floatinput with a new index property
    The index property gives the position of the instance in the InputGrid
    """
    def __init__(self,index=(0,0),*args,**kwargs):
        super(FloatInput,self).__init__(**kwargs)
        self.index = index
        self.multiline = False #enter key calls on_text_validate function
        self.focus = False
        self.size_hint = None,None #force the height and width to be used
        self.height = "30dp"
        self.width = "70dp"
        self.font_size = self.height/2
        self.padding_y = (self.height-self.font_size)/2
        self.use_bubble = True
        self.text = "0.00"
        self.foreground_color = .4,.4,.5,1 #default text color
        
    def on_touch_down(self,touch):
        """
        if touch position is in textinput, focus the current textinput
        and select all texts in the text input for easy editing
        """
        if self.focus==False and self.collide_point(*touch.pos):
            super(FloatInput,self).on_touch_down(touch)
            self.focus = True
            self.select_all()

            
        else: 
            """
            if textinput is on focus or touch postion is outside the textinput
            cancel all selection
            """
            super(FloatInput,self).on_touch_down(touch)
            

    def insert_text(self,substring,from_undo=False):
        """
        allows only integers to be inputed into the textinput 
        """
        s = substring  #let s hold the substring which is the typed text
        try:
            int(s) #ensure the typed text is an integer
            return super(FloatInput,self).insert_text(s,from_undo=from_undo) 
            #insert in textinput if integer
        except: 
            #if typed text is not an integer, do nothing
            pass
    
    def on_text(self,*args):
        """
        change the text color from the default grey to black
        when the text in the textinput is edited
        """
        self.foreground_color = (0,0,0,1)



class InputGrid(GridLayout):
    rows_details_input = ObjectProperty()
    cols_details_input = ObjectProperty()
    def __init__(self,*args,**kwargs):
        super(InputGrid,self).__init__(**kwargs)
        self.padding = "10dp"
        self.spacing = "50dp","10dp"
        self.rows = 5
        self.cols = 5
        self.ti = FloatInput()
        """
        *self.ti holds an instance of the floatinput so that its height
        and width can be accessed and used in the calculation of the 
        inputgrid's height and width.
        *A specific value is needed for the height and width of the inputgrid
        for the scrolling effect to work.
        *Note: self.ti is not added in the input grid, it is only a referencing
        object
        """
        self.height = (
                       (self.ti.height * self.rows)
                       + 
                       (self.padding[1]*4)
                       +
                       (self.spacing[1]*(self.rows-1))
                       )
        
        self.width = (
                      (self.ti.width*self.cols)
                      + 
                      (self.padding[0]*2)
                      +
                      (self.spacing[0]*(self.cols-1))
                      )
        self.size_hint = None,None
        self.fill() #fill the inputgrid with children widgets
        
                
    def fill(self):
        """
        *Fill the inputgrid with the floatinput widget
        *the index of the floatinput should correlate with that of the inputgrid
        for easy accessing of individual floatinput in the inputgrid by method 
        of indexing 
        """
        self.clear_widgets()
        for row in range(self.rows):
            for col in range(self.cols):
                self.add_widget(
                                FloatInput(
                                           index=(row,col),
                                           height = self.height/20,
                                           width = self.width/30
                                           ),
                                index=(row,col)
                                )
    
    def validate(self,called_from):
        if called_from == "rows":
            self.cols_details_input.focus = True
            self.cols_details_input.select_all()
            
        else:
            x = self.rows-1
            y = self.cols-1
            for child in self.children:
                if child.index == (x,y):
                    child.focus = True
                    child.select_all()
                    
    def refill(self):
        self.rows = int(self.rows_details_input.text)
        self.cols = int(self.cols_details_input.text)
        self.height = (
                       (self.ti.height * self.rows)
                       + 
                       (self.padding[1]*4)
                       +
                       (self.spacing[1]*(self.rows-1))
                       )
        
        self.width = (
                      (self.ti.width*self.cols)
                      + 
                      (self.padding[0]*2)
                      +
                      (self.spacing[0]*(self.cols-1))
                      )

        self.fill()

    def on_enter(self,instance):
        """
        *in the initialisation method, multiline is set to False
        * this prevents the cursor from spanning more than a line and
        therfore the floatinputs on_text_validate() method is called whenever
        the enter button is pressed
        *the floatinput's on_text_validate() method calls this method
        *this method moves the focus to the next floatinput and 
        selects all the texts in the floatinput.
        """
        x,y= instance.index #index of the floatinput(instance) that calls the method
        
        if  x!=0 and y == 0:
            """
            if the instance that calls this method is not at the last row
            but at the last column, it should move focus to the instance at the 
            next row and first column
            """
            for child in self.children:
                if child.index == ((x-1),(y+(int(self.cols-1)))):
                    child.focus = True
                    child.select_all()
                    
        elif x == 0 and y==0:
            """
            do nothing if instance is at the last row and last column
            """
            pass
        elif (x == 0 or x != 0) and y!=0:
            """
            if the instance is not at the last column
            move focus to the instance to its right
            """
            for child in self.children:
                if child.index == (x,y-1):
                    child.focus = True
                    child.select_all()
            
                
        
        
        

        
class DetailsInput(FloatInput):
    pass


        
class InputScreen(Screen):
    input_grid = ObjectProperty() #holds the InputGrid object
    op_button = ObjectProperty()
    type_button = ObjectProperty()
    type_drop = ObjectProperty(TypeDrop(max_height=400))
    op_drop = ObjectProperty(OperationDrop(max_height=300))
    def __init__(self,*args,**kwargs):
        super(InputScreen,self).__init__(**kwargs)
        
        
        
        
        
    def add_drop_button(self):
        self.drop_op_box.add_widget(self.op_button)
        self.drop_op_box.add_widget(self.other_button)
    
                
            

#-------------------------------------------------------------------------------
class InputGridApp(App):
    def build(self):
        return InputGrid()
    
if __name__ == "__main__":
    InputGridApp().run()





from tkinter import *


class App:

    def __init__(self, master):
        self._master = master
        # keeps all matrix buttons together using the same 'button=' reference
        # when initializing
        self.btn_matrix = []
        self.listButtonsPressed = []  # keeps track of all the buttons pressed

        '''
        Creating Button Matrix, altering range values for either loop will change the dimension.
        Uses updateChange function when button pressed
        '''
        for matrixColumn in range(8):
            row_matrix = []
            for matrixRow in range(8):
                self.xY = ((7 - matrixColumn), (7 - matrixRow))
                stringXY = str(self.xY)
                button = Button(root, text=stringXY, bg='white',
                                command=lambda x=7 - matrixColumn, y=7 - matrixRow: self.updateChange(x, y))
                button.grid(row=matrixRow, column=matrixColumn)

                row_matrix.append(button)
            self.btn_matrix.append(row_matrix)

        '''
        Creating Print,Clear & Exit Button. Using the appropriate functions (outputPrint,windowClear,windowClose)
        '''
        printButton = Button(root, text='Print', bg='#ffffff',
                             command=self.outputPrint)
        printButton.grid(row=(8), column=(1), pady=10)

        clearButton = Button(root, text='Clear', bg='#ffffff',
                             command=self.windowClear)

        clearButton.grid(row=(8), column=(2), pady=10)

        exitButton = Button(root, text='Exit', bg='white',
                            command=self.windowClose)
        exitButton.grid(row=(8), column=(3), pady=10)

    def updateChange(self, x, y):
        '''
        -Checks Co-ordinate of Button Pressed against Buttons already pressed
        -If new Co-ordniate in that list it revert the button to original colour and removes it from the list
        -if not in the list it add it to the list and changes button colour.
        '''

        xY = list((x, y))

        if xY not in self.listButtonsPressed:
            self.listButtonsPressed.append(list(xY))
            self.btn_matrix[7 - x][7 - y].configure(bg="#000000")

        elif xY in self.listButtonsPressed:
            print(xY)
            self.listButtonsPressed.remove(xY)
            self.btn_matrix[7 - x][7 - y].configure(bg="#ffffff")

    def windowClose(self):
        '''
        -Closes Window When the Close button is pressed
        '''
        root.destroy()

    def outputPrint(self):
        '''
        -Checks if listButtonsPressed is empty
        -If empty it tells user in hte console its empty
        -else it prints the listButtonsPressed
        -- ELSE statement: prints the list of buttons out in SQUARE brackets instead of as a Tuple.
                ALLOWS FOR EASY COPY AND PASTE TO CHARACTER LIBRARY FILE IN UNICORN HAT SIGN
                i.e. Tuples are immutable and the co-ords get manipulated so have to be mutable.
        '''
        if not (self.listButtonsPressed):
            print("List is Empty")
        else:
            print(self.listButtonsPressed)

    def windowClear(self):
        '''
        -Removes all Co-Ordinates from listButtonsPressed
        -Changes all button colours to original colour

        *It loops through the list until empty as not to do so would not clear the list and left co-ordinates
        *User only required to press clear button once

        '''
        while len(self.listButtonsPressed) != 0:
            for point in self.listButtonsPressed:
                x, y = point
                self.btn_matrix[7 - x][7 - y].configure(bg="#ffffff")
                self.listButtonsPressed.remove(point)


root = Tk()
app = App(root)
root.mainloop()

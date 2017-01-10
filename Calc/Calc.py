from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import time


class Calc:

    Calc_Value = 0.0

    Div_Trigger = False
    Mult_Trigger = False
    Add_Trigger = False
    Sub_Trigger = False

    def Button_Press(self, value):

        Entry_Value = self.Number_Entry.get()

        Entry_Value += value

        self.Number_Entry.delete(0, "end")

        self.Number_Entry.insert(0, Entry_Value)

    def Clear_Button_Press(self):

        self.Calc_Value = 0
        self.Number_Entry.delete(0, "end")
        self.Number_Entry.insert(0, "")

    def isfloat(self, Str_Val):
        try:
            float(Str_Val)

            return True

        except ValueError:
            return False

    def Math_Button_Press(self, value):

        if self.isfloat(str(self.Number_Entry.get())):
            self.Div_Trigger = False
            self.Mult_Trigger = False
            self.Add_Trigger = False
            self.Sub_Trigger = False

            self.Calc_Value = float(self.Entry_Value.get())

            if value == "/":
                print("/ Pressed")
                self.Div_Trigger = True

            elif value == "*":
                print("* Pressed")
                self.Mult_Trigger = True

            elif value == "+":
                print("+ Pressed")
                self.Add_Trigger = True

            else:
                print("- Pressed")
                self.Sub_Trigger = True

            self.Number_Entry.delete(0, "end")

    def Button_Equal_Press(self):

        if self.Add_Trigger or self.Sub_Trigger or self.Div_Trigger or self.Mult_Trigger:

            if self.Add_Trigger:
                solution = self.Calc_Value + float(self.Entry_Value.get())
            elif self.Sub_Trigger:
                solution = self.Calc_Value - float(self.Entry_Value.get())
            elif self.Mult_Trigger:
                solution = self.Calc_Value * float(self.Entry_Value.get())
            else:
                if float(self.Entry_Value.get()) != 0:
                    solution = self.Calc_Value / float(self.Entry_Value.get())
                else:
                    print("Divided by Zero\n Will Divde by 1")
                    messagebox.showerror(
                        "Error", "Divided By 0\n\nNumerator Keep & Division cancelled")
                    solution = self.Calc_Value / 1

            #print(self.Calc_Value, " ", float(self.Entry_Value.get()), " ", solution)
            self.Number_Entry.delete(0, "end")

            self.Number_Entry.insert(0, solution)

    def __init__(self, root):

        self.Entry_Value = StringVar(root, value="")

        root.title("John Calc")

        root.geometry("600x300")

        root.resizable(width=False, height=False)

        style = ttk.Style()
        style.configure("TButton",
                        font="Serif 15",
                        padding=10)
        style.configure("TEntry",
                        font="Serif 18",
                        padding=10)

        self.Number_Entry = ttk.Entry(root,
                                      textvariable=self.Entry_Value, width=50)

        self.Number_Entry.grid(row=0, columnspan=4)

        # First Row

        self.Button7 = ttk.Button(root, text="7",
                                  command=lambda: self.Button_Press("7")).grid(row=1, column=0)

        self.Button8 = ttk.Button(root, text="8",
                                  command=lambda: self.Button_Press("8")).grid(row=1, column=1)

        self.Button9 = ttk.Button(root, text="9",
                                  command=lambda: self.Button_Press("9")).grid(row=1, column=2)

        self.Button_Div = ttk.Button(root, text="/",
                                     command=lambda: self.Math_Button_Press("/")).grid(row=1, column=3)

        # Second Row

        self.Button4 = ttk.Button(root, text="4",
                                  command=lambda: self.Button_Press("4")).grid(row=2, column=0)

        self.Button5 = ttk.Button(root, text="5",
                                  command=lambda: self.Button_Press("5")).grid(row=2, column=1)

        self.Button6 = ttk.Button(root, text="6",
                                  command=lambda: self.Button_Press("6")).grid(row=2, column=2)

        self.Button_Mult = ttk.Button(root, text="*",
                                      command=lambda: self.Math_Button_Press("*")).grid(row=2, column=3)

        # Third Row

        self.Button1 = ttk.Button(root, text="1",
                                  command=lambda: self.Button_Press("1")).grid(row=3, column=0)

        self.Button2 = ttk.Button(root, text="2",
                                  command=lambda: self.Button_Press("2")).grid(row=3, column=1)

        self.Button3 = ttk.Button(root, text="3",
                                  command=lambda: self.Button_Press("3")).grid(row=3, column=2)

        self.Button_Add = ttk.Button(root, text="+",
                                     command=lambda: self.Math_Button_Press("+")).grid(row=3, column=3)

        # Forth Row

        self.Button_Clear = ttk.Button(root, text="AC",
                                       command=lambda: self.Clear_Button_Press()).grid(row=4, column=0)

        self.Button0 = ttk.Button(root, text="0",
                                  command=lambda: self.Button_Press("0")).grid(row=4, column=1)

        self.Button_Equal = ttk.Button(root, text="Enter",
                                       command=lambda: self.Button_Equal_Press()).grid(row=4, column=2)

        self.Button_Sub = ttk.Button(root, text="-",
                                     command=lambda: self.Math_Button_Press("+")).grid(row=4, column=3)

        # Fith Row

        self.Button_Decimal = ttk.Button(root, text=".",
                                         command=lambda: self.Button_Press(".")).grid(row=5, column=1)


root = Tk()

Calculator = Calc(root)

root.mainloop()

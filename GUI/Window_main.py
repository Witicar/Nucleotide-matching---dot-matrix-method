import tkinter

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from Create_Matrix.CreateArrayFromFile import create_list
from tkinter import filedialog


class ButtonRoot(FloatLayout):
    def takeFile(self):
        root = tkinter.Tk()
        root.withdraw()
        path = filedialog.askopenfilename(filetypes = (("Text Files", "*.txt"),("All Files","*.*")))
        nucleotide_array_one = create_list(path)
        print(nucleotide_array_one)


class MatrixComparison(App):
    def build(self):
        return ButtonRoot()


import tkinter

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from Create_Matrix.CreateArrayFromFile import *
from tkinter import filedialog


class ButtonRoot(FloatLayout):
    def take_file(self, textbox):
        root = tkinter.Tk()
        root.withdraw()
        path = filedialog.askopenfilename(filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")))
        if path != '':
            read_text = read_file(path)
            nucleotide_array = create_nucleotide_list(read_text)
            nucleotide_sequence = nucleotide_maker_from_string(read_text)
            textbox.text = str(nucleotide_sequence)
            return nucleotide_array


class MatrixComparison(App):
    def build(self):
        return ButtonRoot()


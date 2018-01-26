import numpy as np


def _open_file(source_str):
    file = open(source_str, "r")
    return file


def _read_file(file):
    text_container = file.readline()
    return text_container


def _nucleotyde_maker_from_string(protein_str):
    text = ""
    increment = 0
    for t in protein_str:
        container = protein_str[increment]
        if container.isalpha():
            text += container
        increment += 1
    return text


def create_list(source):
    file = _open_file(source)
    protein = np.array(list(_nucleotyde_maker_from_string(_read_file(file))))
    file.close()
    return protein
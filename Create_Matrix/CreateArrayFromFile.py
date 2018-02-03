import numpy as np


def _open_file(source_str):
    file = open(source_str, "r")
    return file


def _close_file(file):
    file.close()


def read_file(path):
    file = _open_file(path)
    text_container = file.readline()
    _close_file(file)
    return text_container


def nucleotide_maker_from_string(sequence_str):
    text = ""
    increment = 0
    for t in sequence_str:
        container = sequence_str[increment]
        if container.isalpha():
            text += container
        increment += 1
    return text


def create_nucleotide_list(sequence):
    protein = np.array(list(nucleotide_maker_from_string(sequence)))
    return protein

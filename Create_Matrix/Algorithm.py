import numpy as np


def matrix_create(nucleotide_array_one, nucleotide_array_two):
    matrix = np.zeros((len(nucleotide_array_one),len(nucleotide_array_two)))
    return matrix


def dot_matrix_algorithm(nucleotide_array_one, nucleotide_array_two):
    matrix = matrix_create(nucleotide_array_one, nucleotide_array_two)
    for index_out, item_out in enumerate(nucleotide_array_one):
        for index_in, item_in in enumerate(nucleotide_array_two):
            if item_out == item_in:
                matrix[index_out][index_in] = 1
    print(matrix)
    return matrix

from Create_Matrix.CreateArrayFromFile import create_list
from Create_Matrix.Algorithm import dot_matrix_algorithm

nucleotide_array_one = create_list("protein_one.txt")
nucleotide_array_two = create_list("protein_two.txt")

dot_matrix_algorithm(nucleotide_array_one, nucleotide_array_two)
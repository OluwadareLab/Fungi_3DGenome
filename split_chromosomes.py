import numpy as np

def read_genome_file(file_path):
    with open(file_path, 'r') as file:
        content = file.readlines()
    return content

def split_genome_matrix(matrix, chromosome_lengths):
    split_matrices = []

    start_index = 0
    for length in chromosome_lengths:
        end_index = start_index + length
        chromosome_matrix = matrix[start_index:end_index, start_index:end_index]
        split_matrices.append(chromosome_matrix)
        start_index = end_index

    return split_matrices

def save_matrices_to_files(split_matrices):
    for i, chromosome_matrix in enumerate(split_matrices):
        np.savetxt(f'chromosome_{i + 1}_matrix.txt', chromosome_matrix, fmt='%.18f')

def main():
    file_path = 'NKL2-delta.txt' # Input filename of the genome HiC matrix
    chromosome_lengths = [499, 219, 264, 300, 341, 211, 213] # Specify the lengths of chromosomes in the genome

    matrix_content = read_genome_file(file_path)
    matrix = np.array([list(map(float, line.split())) for line in matrix_content])

    split_matrices = split_genome_matrix(matrix, chromosome_lengths)

    save_matrices_to_files(split_matrices)

if __name__ == "__main__":
    main()

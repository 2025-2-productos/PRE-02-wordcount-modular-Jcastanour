# obtain a list of files in the input directory
import sys

from ._internals.count_words import count_words
from ._internals.preprocess_lines import preprocess_lines
from ._internals.read_all_lines import read_all_lines
from ._internals.split_into_words import split_into_words
from ._internals.write_word_counts import write_word_counts


def main(input_folder=None, output_folder=None):
    # Caso 1: main() llamado directamente → usar carpetas por defecto
    if input_folder is None or output_folder is None:

        # Caso 2: si fue llamado por CLI con argumentos
        if len(sys.argv) == 3:
            input_folder = sys.argv[1]
            output_folder = sys.argv[2]
        else:
            # Defaults para los tests
            input_folder = "data/input"
            output_folder = "data/output"

    ## read all lines
    all_lines = read_all_lines(input_folder)

    ### preprocess lines
    all_lines = preprocess_lines(all_lines)

    ### split in words
    words = split_into_words(all_lines)

    ### count words
    counter = count_words(words)

    ### write word counts
    write_word_counts(counter, output_folder)


if __name__ == "__main__":
    main()

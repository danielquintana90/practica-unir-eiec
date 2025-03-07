"""
License: Apache
Organization: UNIR
"""

import os
import sys

DEFAULT_FILENAME = "palabras.txt"
DEFAULT_DUPLICATES = False
DEFAULT_ORDER = "asc"

def sort_list(items, ascending=True, remove_duplicates=False):
    if not isinstance(items, list):
        raise RuntimeError(f"No puede ordenar {type(items)}")

    if remove_duplicates:
        items = list(set(items))

    return sorted(items, reverse=(not ascending))


if __name__ == "__main__":
    filename = DEFAULT_FILENAME
    remove_duplicates = DEFAULT_DUPLICATES
    order = DEFAULT_ORDER

    if len(sys.argv) == 4:
        filename = sys.argv[1]
        remove_duplicates = sys.argv[2].lower() == "yes"
        order = sys.argv[3].lower()
    else:
        print("Se debe indicar el fichero como primer argumento")
        print("El segundo argumento indica si se quieren eliminar duplicados")
        print("El tercer argumento indica el orden: 'asc' para ascendente o 'desc' para descendente")        
        sys.exit(1)

    print(f"Se leerán las palabras del fichero {filename}")
    file_path = os.path.join(".", filename)
    if os.path.isfile(file_path):
        word_list = []
        with open(file_path, "r") as file:
            for line in file:
                word_list.append(line.strip())
    else:
        print(f"El fichero {filename} no existe")
        word_list = ["ravenclaw", "gryffindor", "slytherin", "hufflepuff", "ravenclaw"]


    ascending = order == "asc"
    print(sort_list(word_list, ,ascending=ascending, remove_duplicates=remove_duplicates))


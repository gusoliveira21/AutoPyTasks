import matplotlib.pyplot as plt
import re
from collections import defaultdict

def add_to_tree(base, parts):
    """ Recursively add parts of the path to the nested dictionary """
    for part in parts:
        base = base[part]

def parse_structure(lines):
    """ Parse the indented structure into a nested dictionary """
    tree = lambda: defaultdict(tree)
    root = tree()
    
    # Convert indentation into depth levels
    for line in lines:
        parts = line.strip().split('/')
        # Remove empty strings from parts, which represent directories
        parts = [part for part in parts if part]
        add_to_tree(root, parts)
    return root

def plot_tree(data, parent_name='', ax=None, pos=None, level=0, y_offset=-1, x_offset=0.5):
    if pos is None:
        pos = {parent_name: (0, 0)}
    if ax is None:
        fig, ax = plt.subplots(figsize=(20, 10))
        ax.axis('off')
        
    y_pos = pos[parent_name][1] + y_offset
    next_x = level + x_offset
    for k, v in sorted(data.items()):
        pos[k] = (next_x, y_pos)
        ax.plot([level, next_x], [pos[parent_name][1], y_pos], 'k-', zorder=1)
        y_pos += y_offset
        plot_tree(v, k, ax, pos, next_x, y_offset, x_offset)
    ax.text(level, pos[parent_name][1], parent_name, ha='right' if level else 'center', va='center', zorder=2)

    # Ajuste dos limites
    ax.set_xlim(left=-x_offset, right=next_x + x_offset)
    ax.set_ylim(top=0, bottom=y_pos + y_offset)

    return ax

# Solicita ao usuário o caminho do arquivo de texto
filepath = input("Digite o caminho do arquivo de texto com a estrutura de diretórios: ")

# Parse the structure from the file
with open(filepath, 'r') as f:
    lines = f.readlines()

structure = parse_structure(lines)

# Assumindo que a estrutura possui um nível raiz com uma única entrada
root_name = next(iter(structure))  # Get the first key in the dictionary
ax = plot_tree(structure[root_name], parent_name=root_name, y_offset=-2)  # Ajuste do espaçamento vertical para evitar sobreposição
plt.tight_layout()
plt.show()

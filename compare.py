import numpy
import ast
from pprint import pprint
def leve(first_str, second_str):
    n, m = len(first_str), len(second_str)
    if n > m:
        first_str, second_str = second_str, first_str
        n, m = m, n

    current_row = range(n + 1)
    for i in range(1, m + 1):
        previous_row, current_row = current_row, [i] + [i - 1] * n
        for j in range(1, n + 1):
            add = previous_row[j] + 1
            delete = current_row[j - 1] + 1
            change = previous_row[j - 1]
            if first_str[j - 1] != second_str[i - 1]:
                change += 1
            current_row[j] = min(add, delete, change)

    return current_row[n]


def main():
#     with open("file_2.py", "r") as source:
#         ast_tree = ast.parse(source.read())
#
#     analysis = Analyzer()
#     analysis.visit(ast_tree)
#     analysis.report()
#
#
# class Analyzer(ast.NodeVisitor):
#     def __init__(self):
#         self.stats = {"import": [], "from": []}
#
#     def node_visit(self, node):
#         for alias in node.names:
#             self.stats["import"].append(alias.name)
#         self.generic_visit(node)
#
#     def node_visitFrom(self, node):
#         for alias in node.names:
#             self.stats["from"].append(alias.name)
#         self.generic_visit(node)
#
#     def report(self):
#         pprint(self.stats)
    with open('file.py', 'r') as file:
        data_f = file.read()
    with open('file_2.py', 'r') as file:
        data_t = file.read()

    print(leve(data_f, data_t))

if __name__ == '__main__':
    main()
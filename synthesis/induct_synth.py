import astor
import ast
import pandas as pd

MAP_OPS = pd.read_csv("models/mappers.csv")
REDUCE_OPS = pd.read_csv("models/reducers.csv")
OPERATION_LIST = [ast.Assign, ast.AugAssign]


def extract_operations(for_node: ast.For):
    return [x for x in ast.walk(for_node) if type(x) in OPERATION_LIST]  

FILEPATH = 'synthesis/test_input.py'
code_file = astor.code_to_ast.parse_file(FILEPATH)
with open(FILEPATH, "rt") as fin:
    tree = ast.parse(fin.read())

detected_fragment = [node for node in tree.body if isinstance(node, ast.For)]

print(detected_fragment[0])
all_operations =  extract_operations(detected_fragment[0])

print(all_operations)



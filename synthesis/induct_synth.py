import astor
import ast
import pandas as pd
import shutil


MAPS_COUNTER = 0
REDuce_COUNTER = 0
MAP_OPS = pd.read_csv("models/mappers.csv")
REDUCE_OPS = pd.read_csv("models/reducers.csv")
OPERATION_LIST = [ast.Assign, ast.AugAssign]
COPY_FILEPATH = "verifier/test_gen.py"

def extract_operations(for_node: ast.For):
    return [x for x in ast.walk(for_node) if type(x) in OPERATION_LIST]  


def copy_progam(filepath):
    shutil.copyfile(filepath, COPY_FILEPATH)


def convert_ops_pyspark(node):
    print("HERE")
    current_operation = MAP_OPS[MAPS_COUNTER]
    lambda_expression =  "lambda each: each" + str("*") + str(node.value.right.target) 
    exp = current_operation.replace("##\n##", lambda_expression)
 
    
FILEPATH = 'synthesis/func_test.py'
code_file = astor.code_to_ast.parse_file(FILEPATH)
copy_progam(FILEPATH)


with open(COPY_FILEPATH, "rt") as fin:
    tree = ast.parse(fin.read())

function_node = [ node for node in tree.body if isinstance(node, ast.FunctionDef)]

print(function_node)
detected_fragment = [node for node in ast.walk(function_node[0]) if isinstance(node, ast.For)]

print(detected_fragment)
all_operations =  extract_operations(detected_fragment[0])

a = convert_ops_pyspark(all_operations[0])


#print(astor.to_source(all_operations[0]))



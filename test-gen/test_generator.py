import os
import subprocess
import re

VIRTUAL_ENV_PATH = "env-test/bin"
def convert_code_fragments_to_file(dataset_name: str, code_fragment: str, scope_variables: []):
    variables = ""
    imports =  "from typing import List"
    for each_variable in scope_variables:
        variables += str(each_variable) + " = 0 \n"

    # READ THE SKELETON FILE
    sk_file = open("temp-source-code.txt", "rt", encoding='utf-8')
    data = sk_file.read()
    sk_file.close()

    # REPLACE IMPORTS IF NEEDED
    # TODO -> Make this dynamic
    data = data.replace("##IMPORTS", imports)

    # REPLACE THE DATASET
    data  = data.replace("##DATASET", dataset_name + ": List[int]")

    # REPLACE THE SCOPE VARIABLES
    data = data.replace("##VARIABLES", variables)

    # REPLACE THE RETURN VARIABLE
    # TODO -> MAKE RETURN DYNAMIC
    data = data.replace("##RETURN", "return " +str(variables[0]))

    # REPLACE THE FUNCTION BODY
    code_fragment = code_fragment.replace("\t", '    ')
    data = data.format(code_fragment)
    #data = data.replace("##FUN_BODY", code_fragment)
    # data = [x if str(x) != "    ##FUN_BODY" else  code_fragment for x in data.split("\n")]
    # data = "\n".join(data)
    #data = data.replace('\t', "    ")
    #data = data.replace("{}", code_fragment)
    # print("\n".join(d))

    # CREATE OUTPUT FILE 1
    gen_file = open("temp-gen.py", "wt")
    gen_file.write(data)
    gen_file.close()

def generate_test_cases(input_filePath,output_filepath):
    # Activate Virtual Environment
    subprocess.Popen(VIRTUAL_ENV_PATH, 'activate_this.py')
    print("here")

fragment = "for i in nums:\n\t\ts+=i"
vars = ["s"]
dataset_name = "nums"
#convert_code_fragments_to_file(dataset_name=dataset_name, code_fragment=fragment, scope_variables=vars)
generate_test_cases("A","B")
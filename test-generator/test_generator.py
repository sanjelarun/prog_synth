import os
import pandas as pd
WORKING_DIR = "/test-generator"
TEST_GEN_DIRECTORY = "test-gen/generate_tests"
MODULE_NAME = "temp-gen"


def insert_dash(string, index, new_string):
    return string[:index] + new_string + string[index:]

def convert_code_fragments_to_file(dataset_name: str, code_fragment: str, scope_variables: []):
    variables = ""
    imports = "from typing import List"
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
    data = data.replace("##DATASET", dataset_name + ": List[int]")

    # REPLACE THE SCOPE VARIABLES
    data = data.replace("##VARIABLES", variables)
    code_fragment = code_fragment.replace('    ', '\t\t')
    print(repr(code_fragment))
    # index_of_fun = data.index("##FUN_BODY")
    # for each_line in code_fragment.split('\n'):
    #     print(insert_dash(data, index_of_fun, each_line))

    data = data.replace("##FUN_BODY", code_fragment)
    # REPLACE THE RETURN VARIABLE
    # TODO -> MAKE RETURN DYNAMIC
    data = data.replace("##RETURN", "return " + str(scope_variables[0]))

    # REPLACE THE FUNCTION BODY
    #print(code_fragment)


    # CREATE OUTPUT FILE 1
    gen_file = open("temp-gen.py", "wt")
    gen_file.write(data)
    gen_file.close()

    # Auto Indentation the Python file
    cmd = "autopep8 /home/sanjelarun/prog_synth/prog_synth/test-gen/temp-gen.py --in-place --pep8-passes 2000 --verbose"
    stream = os.popen(cmd)
    print(stream.read())


def generate_test_cases():
    # SETTING PYNGUIN ENVIRONMENT VARIABLE
    os.environ["PYNGUIN_DANGER_AWARE"] = ""

    # GENERATING TEST CASES USING PYNGUIN
    cmd = "pynguin --project-path " + WORKING_DIR + " --output-path " + TEST_GEN_DIRECTORY + " --module-name temp-gen -v"
    stream = os.popen(cmd)
    print()


def extract_only_test(generate_file_path="test-gen/generate_tests/test_temp-gen.py"):

    with open('/test-generator/temp-gen.py') as gen_in:
        allLines = gen_in.read()

    with open('/test-generator/test-gen/generate_tests/test_temp-gen.py') as fin:
        data = fin.read()
        data = data.replace("import temp-gen as module_0", allLines)
        data = data.replace("module_0.", " ")

    with open("code_with_test.py", 'w') as outputFile:
        outputFile.write(data)





df = pd.read_csv('/home/sanjelarun/prog_synth/prog_synth/models/train.csv', sep="#")
print(df.head())

a = df.loc[0]
code = a[0].replace('\\n','\n').replace('\\t','\t')
convert_code_fragments_to_file(a[2],code, [a[3]])
generate_test_cases()
extract_only_test()
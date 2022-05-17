from comp_gen import *

test_file = "component_generator/example-1.py"

root = convert_graph_to_struct(test_file)


print(root)

root.print_graph()
root.get_graph_pdf()
import d3.model.tools as mt
import os

def convert_to_obj(file_name):
    input_path = os.path.join("uploads", file_name)
    obj_file_name = file_name.split(".")[0] + ".obj"
    output_path = os.path.join("out", obj_file_name)
    result = mt.convert(input_path, output_path, None)
    with open(output_path, 'w') as f:
        f.write(result)

import re
from string import Template 

def extract_data(out_file):
    with open(out_file, "r", encoding="utf-8") as file:
        out_content = file.readlines()
    
    #Finding AXX, BYY, CZZ
    rot_constants_pattern = r"AXX=\s*([\d.E+-]+)\s*BYY=\s*([\d.E+-]+)\s*CZZ=\s*([\d.E+-]+)"
    #Assigning to a tuple
    rot_constants_match = re.search(rot_constants_pattern, "".join(out_content))

    #Tuple to constants
    if rot_constants_match:
        a_const, b_const, c_const = rot_constants_match.groups()

    a_const, b_const, c_const = map(float, (a_const, b_const, c_const))
    
def create_fortran_file(filename, content):
    """
    Creates a .f file with the given filename and content.

    Args:
        filename (str): The name of the .f file to create (e.g., "my_program.f").
        content (str): The content to write into the file.
    """
    try:
        with open(filename, "w") as file:
            file.write(content)
        print(f"File '{filename}' created successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")    






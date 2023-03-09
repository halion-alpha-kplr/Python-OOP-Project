import json
from unidecode import unidecode
import os

def json_dict_from_file():
    local_path = os.path.dirname(os.path.abspath(__file__))
    json_data = json.load(open(os.path.join(local_path, 'json_data.json'), "rb"))
    json_str = json.dumps(json_data)
    json_data = unidecode(json_str)
    json_dict = json.loads(json_data)
    return json_dict

def generate_class_def(class_name: str, attrs:dict, superclass_name:str,superclass_args:list=[]):    
    
    constructor_args = []
    constructor_def = ""
    has_attributes = False

    class_template = f"class {class_name}"

    if superclass_name:        
        class_template += f"({superclass_name})"
    
    class_template += ":\n"

    for attr_name in attrs.keys():
        if attr_name != "subclasses":
            has_attributes = True
            constructor_args.append(attr_name)
            constructor_def += f"\n\t\tself.{attr_name} = {attr_name}"

    if class_name == "Product":
        constructor_def += "\n\t\tself.name=type(self).__name__"

    if has_attributes:
        constructor_template = f"\tdef __init__(self, {', '.join(constructor_args+superclass_args)}):"

        if len(superclass_args)>0:
            constructor_template +=f"\n\t\tsuper().__init__({', '.join(superclass_args)})"

        constructor_template +=constructor_def
    
    else:
        if len(superclass_args)>0:
            constructor_template = f"\tdef __init__(self, {', '.join(superclass_args)}):"
            constructor_template +=f"\n\t\tsuper().__init__({', '.join(superclass_args)})"
      
        else:    
            constructor_template = "\tpass"

    return class_template + constructor_template + "\n\n"

if __name__ == '__main__':

    test_solution = generate_class_def("test",json_dict_from_file(),"test",)
    print(test_solution)
    print(json_dict_from_file())
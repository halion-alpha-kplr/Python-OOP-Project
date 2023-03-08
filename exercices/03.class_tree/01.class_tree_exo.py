import json
from unidecode import unidecode
from treelib import Tree
import os


def json_dict_from_file():
    local_path = os.path.dirname(os.path.abspath(__file__))
    json_data = json.load(open(os.path.join(local_path, 'json_data.json'), "rb"))
    json_str = json.dumps(json_data)
    json_data = unidecode(json_str)
    json_dict = json.loads(json_data)
    return json_dict

def create_tree_from_dict(json_dict):
    global tree 
    tree = Tree()

    root_node_id = "root"
    root_node_name = "Product Classes Hierarchy"
    tree.create_node(root_node_name, root_node_id)

    recusive_tree_from_json(json_dict, root_node_id)

    return tree

def recusive_tree_from_json(json_dict, parent_node_id):
    for class_name, class_attrs in json_dict.items():            
            class_node_id = class_name
            class_node_name = class_name

            tree.create_node(class_node_name, class_node_id, parent=parent_node_id)

            if "subclasses" in class_attrs:
                recusive_tree_from_json(class_attrs["subclasses"], class_node_id)

def main():
    
    json_dict = json_dict_from_file()
    my_tree = create_tree_from_dict(json_dict)

    my_tree.show()

if __name__ == '__main__':
    main()
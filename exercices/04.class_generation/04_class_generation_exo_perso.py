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

def generate_class_def(nom_classe: str, attributs: dict, nom_superclasse: str, args_superclasse: list = []) -> str:
    args_constructeur = [] 
    definition_constructeur = ""
    has_attributs = False
    modele_classe = f"class {nom_classe}"

if nom_superclasse:
        modele_classe += f"({nom_superclasse})"
        modele_classe += ":\n"

    for nom_attribut in attributs.keys():
        if nom_attribut != "subclasses":
            has_attributs = True
            args_constructeur.append(nom_attribut)
            definition_constructeur += f"\n\t\tself.{nom_attribut} = {nom_attribut}" 

    if nom_classe == "Product":
        definition_constructeur += "\n\t\tself.name=type(self).__name__"
if has_attributs:
        modele_constructeur = f"\tdef __init__(self, {', '.join(args_constructeur + args_superclasse)}):" 
        if len(args_superclasse) > 0:
            modele_constructeur += f"\n\t\tsuper().__init__({', '.join(args_superclasse)})"

        modele_constructeur += definition_constructeur   
    else: 
        if len(args_superclasse) > 0:
            modele_constructeur = f"\tdef __init__(self, {', '.join(args_superclasse)}):"
            modele_constructeur += f"\n\t\tsuper().__init__({', '.join(args_superclasse)})"     
        else:    
            modele_constructeur = "\tpass"
    return modele_classe + modele_constructeur + "\n\n"

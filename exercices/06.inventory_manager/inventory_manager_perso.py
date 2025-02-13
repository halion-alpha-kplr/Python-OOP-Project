#La classe "InventoryManager" est une classe qui permet de gérer un inventaire de produits. 
from inventory_product_entry_perso import *

class InventoryManager:
    # Initialisation de la classe
    def __init__(self):
        # Vous initialisez un dictionnaire 'inventory' qui stocke l'inventaire de tous les produits
        # Il prend comme clé le nom du produit, et la valeur est un objet InventoryProductEntry
        self.inventory : Dict[str, InventoryProductEntry] = {}

    #Méthode product_exists
    """"
    La fonction prend un objet Product en entrée et vérifie si son nom est une clé dans le dictionnaire self.inventory. 
    Si c'est le cas, la fonction retourne True, sinon elle retourne False.
    """
    def product_exists(self,product:Product):
        if product in self.inventory:
            return True
        return False

    #Méthode add_product
    """
    La méthode add_product est utilisée pour ajouter un nouveau produit à l'inventaire.
    Elle prend en argument un objet Product et une quantité initiale.
    """
    def add_product(self, product:Product, quantity):
        
        If product in self.inventory :
            print("Ce produit existe déja dans la base.")
            self.inventory += {product:quantity}
 
    #Méthode remove_product
    """
    La méthode remove_product est utilisée pour supprimer un produit de l'inventaire.
    Elle prend en argument un nom de produit et supprime l'entrée correspondante dans le dictionnaire 'inventory'.
    """
    def remove_product(self, product_name):
        if product_exists(self,product_name) == True :
            self.inventory.remove(product_name)
        print("Le produit n'a pas été trouvé dans l'inventaire !")

    
    #Méthode sell_product
    """
    La méthode sell_product est utilisée pour vendre une quantité donnée d'un produit.
    Elle prend en argument le nom du produit et la quantité à vendre.
    """
    
    def sell_product(self, product_name, quantity):
        for key in self.inventory :
            if product_exists(self,product_name) == True :
               inventory_product_entry_perso.sell(quantity) 
            print("Le produit n'a pas été trouvé, la vente a échoué !")

    
    #Méthode restock_product
    """
    La méthode restock_product est utilisée pour restocker une quantité donnée d'un produit.
    Elle prend en argument le nom du produit et la quantité à restocker.
    """
    def restock_product(self, product_name, quantity):
        if product_name in self.inventory == True:
            inventory_product_entry_perso.restock(self, quantity)
            print("Le restock a fonctionné")
        add_product(self, product_name, quantity=0)
        inventory_product_entry_perso.restock(self, reception_quantity =0):


        #Vérifier si le produit existe déjà dans l'inventaire
        #Si le produit est trouvé, appeler la méthode 'restock' de l'objet InventoryProductEntry correspondant avec la quantité à restocker
        #Si le réapprovisionnement est réussi, afficher un message de confirmation
        #Sinon, on appelle la méthode add_product pour ajouter le produit en stock avec une quantité nulle et on rappelle la fonction restock_product pour le restocker
    
    
    #Méthode get_product
    """
    La méthode get_product retourne toutes les informations liées au produit en faisant une recherche par son nom.
    Elle prend en entrée un nom de produit.
    """
    def get_product(self, name):
        for inventory_product_entry_key in self.inventory :
            if inventory_product_entry_key == name
                return self.inventaire[inventory_product_entry_key].product
        
        print("Le produit n'existe pas !")
        """
        pour chaque inventory_product_entry_key dans self.inventory:
            si inventory_product_entry_key == nom de produit:
                retourner self.inventaire[inventory_product_entry_key].product
        afficher un message pour indiquer que le produit n'existe pas
        """

    #Méthode list_products
    """
    La méthode list_products(self) parcourt tous les produits de l'inventaire 
    et affiche les informations relatives à chacun d'entre eux (nom, quantité disponible, prix unitaire, coût unitaire, prix de vente unitaire, bénéfice unitaire). 
    """
    def list_products(self):
        for key in self.inventory :
            print(self.inventory.value)
        return self.inventory
        """
        pour chaque clé du dictionnaire 'inventory':
            afficher la valeur correspondante à cette clé
        retourner le dictionnaire inventaire
        """

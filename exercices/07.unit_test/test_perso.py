#Importer les bibliothèques nécessaires
import sys
import unittest
sys.path.extend(['.','..'])

#Import des classes à tester
from product_classes import Chaise, Pantalon
from inventory_manager_perso import InventoryManager

#Définition de la classe de test
class TestInventoryManager(unittest.TestCase):
    """
    Méthode setUp est une méthode spéciale dans le module unittest de Python.
    Elle est appelée avant chaque méthode de test définie dans une classe de test et sert à mettre en place l'état initial pour les tests.
    Elle est utilisée pour initialiser des objets que les méthodes de test vont utiliser.
    """
    def setUp(self):
        # Instanciation de l'objet InventoryManager
        self.inventory_manager = InventoryManager()
        # Instanciation d'objets Chaise et Pantalon pour les tests
        self.chaise = Chaise("materiau2", "couleur2", "dimension2", 50, 100, "Ikea")
        self.pantalon = Pantalon("M", "noir", "jeans", 150, 200,"Zara")

    # Test de la méthode add_product de la classe InventoryManager
    def test_add_product(self):
        
        add_product(self,chaise,5)
        self.assertIn(chaise,self.inventory_manager)


# Exécuter le code     
if __name__ == '__main__':
    unittest.main()
    test_add_product()
    print(self.inventory_manager)    

# Vous allez créer une classe InventoryProductEntry qui a pour role 
# de représenter une entrée d'inventaire pour un produit spécifique.

class InventoryProductEntry:
    def __init__(self, inventory_product : Product, inventory_quantity):
        self.inventory_product = inventory_product
        self.inventory_quantity = inventory_quantity
        self.sales = 0
        self.expenses = 0

    def sell(self, sales_quantity):
        if self.inventory_quantity < sales_quantity :
            return False
        else :
            self.inventory_quantity = self.inventory_quantity-sales_quantity
            self.sales = self.inventory_product.price*sales_quantity
            return True
        
    def restock(self, reception_quantity):
        self.inventory_quantity = self.inventory_quantity+reception_quantity 
        self.sales = reception_quantity*self.inventory_product.price

    def __repr__(self):
        print(self.inventory_product.price,self.inventory_product.marque,self.inventory_quantity,self.inventory_product.price)
        # Retourner une chaîne de caractères formatée contenant le nom du produit, la marque, la quantité en stock et le prix du produit.
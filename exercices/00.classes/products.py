class Product:
    def __init__(self, cost, price, marque):
        self.cost = cost
        self.price = price
        self.marque = marque

class Meubles(Product):
    def __init__(self, materiaux, couleur, dimensions,nom):
        super().__init__(cost, price, marque)
        self.materiaux = materiaux
        self.couleur = couleur
        self.dimensions = dimensions
        self.nom = nom
    
class Canape(Meubles):
    def __init__(self):
        super().__init__(cost, price, marque, materiaux, couleur, dimensions)

class Chaise(Meubles):
    def __init__(self):
        super().__init__(cost, price, marque, materiaux, couleur, dimensions)

class Table(Meubles):
    def __init__(self):
        super().__init__(cost, price, marque, materiaux, couleur, dimensions)

canape1 = Canape(1000,2000,"SIESTA","Cuir","Blanc","200*100*80","Canape")
canape2 = Canape(800,1600,"SIESTA","Tissu","Bleu","150*90*70","Canape")
chaise1 = Chaise(50,100,"PEPOUSE","Plastique","Rouge","50*50*70","Chaise")
chaise2 = Chaise(75,150,"PEPOUSE","Metal","Gris","60*60*80","Chaise")
table1 = Table(250,500,"TEX","Bois","Chêne","150*80*75")
table2 = Table(350,700,"TEX","Verre","Transparent","120*60*75")

print(canape1.couleur, canape1.cost, canape1.price, canape1.dimensions)
print(canape2.couleur, canape1.cost, canape1.price, canape1.dimensions)
print(table1.couleur, canape1.cost, canape1.price, canape1.dimensions)
print(table2.couleur, canape1.cost, canape1.price, canape1.dimensions)
#test de sauvegarde

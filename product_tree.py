from recipes import *
from buildings import *
import networkx as nx
import matplotlib.pyplot as plt
import math


class Product_Tree(nx.DiGraph):

    def __init__(self, item_name, rate):
        super().__init__()
        self.layers = []

        rec = allRecipes[item_name]
        buildings = [Building(rec.building) for i in range(math.ceil(rate/rec.rate))]
        efic = rate/(len(buildings)*rec.rate)
        for b in buildings:
            self.add_node(b, efic=efic)
        self._add_layer(rec, buildings, efic)

    def _add_layer(self, rec, buildings, efic):
        self.layers.append(buildings)

        for ingredient, count in rec.ingredients.items():
            pre_rec = allRecipes[ingredient]
            pre_buildings = [Building(pre_rec.building) for i in range(math.ceil((count*rate*efic)/pre_rec.rate))]
            pre_efic = (len(buildings)*rec.rate*count*efic)/(len(pre_buildings)*pre_rec.rate)
            for b in pre_buildings:
                self.add_node(b, efic=pre_efic)
            
            gcd = math.gcd(len(buildings), len(pre_buildings))
            for b in buildings:
                group = b//(len(buildings)//gcd)
                for pre_b in pre_buildings[group*(len(pre_buildings)//gcd):(group+1)*(len(pre_buildings)//gcd)]:
                    self.add_edge(pre_b, b)

            self._add_layer(pre_rec, pre_buildings, pre_efic)

    def show(self):
        nx.draw(self, with_labels=True)
        plt.show()
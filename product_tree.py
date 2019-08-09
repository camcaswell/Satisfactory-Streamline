from recipes import *
from buildings import *
import networkx as nx
import matplotlib.pyplot as plt
import math


class ProductTree(nx.DiGraph):

    def __init__(self, item_name, required_output):
        super().__init__()
        self.pos = {}
        rec = allRecipes[item_name]
        self.heads = [BuildingNode(rec=rec, depth=0) for i in range(math.ceil(required_output/rec.rate))]
        efic = required_output/(len(self.heads)*rec.rate)
        for node in self.heads:
            node.efic = efic
            self.add_node(node)
        self._add_layer(rec, self.heads, efic, 1)

    def _add_layer(self, rec, buildings, efic, depth):
        for ingredient, count in rec.ingredients.items():
            pre_rec = allRecipes[ingredient]
            required_output = len(buildings)*efic*(rec.rate/rec.makes)*count
            pre_buildings = [BuildingNode(rec=pre_rec, depth=depth) for i in range(math.ceil((required_output/pre_rec.rate)))]
            pre_efic = required_output/(len(pre_buildings)*pre_rec.rate)
            for node in pre_buildings:
                node.efic = pre_efic
                self.add_node(node)
            
            gcd = math.gcd(len(buildings), len(pre_buildings))
            for idx, b in enumerate(buildings):
                group = idx//(len(buildings)//gcd)
                for pre_b in pre_buildings[group*(len(pre_buildings)//gcd):(group+1)*(len(pre_buildings)//gcd)]:
                    self.add_edge(pre_b, b)

            self._add_layer(pre_rec, pre_buildings, pre_efic, depth+1)

    def _get_color_map(self):
        cmap = []
        for node in self:
            if hasattr(node, 'building'):
                cmap.append(ProductTree.color_of(node.building))
            else:
                cmap.append(ProductTree.color_of(node))
        return cmap

    def color_of(building):
        if 'Miner' in building:
            return 'tan'
        elif 'Smelter' in building:
            return 'orange'
        elif 'Foundry' in building:
            return 'silver'
        elif 'Constructor' in building:
            return 'yellow'
        elif 'Assembler' in building:
            return 'red'
        elif 'Manufacturer' in building:
            return 'blue'
        elif 'Oil Refinery' in building:
            return 'green'
        elif 'Nuclear Power Plant' in building:
            return 'pink'
        elif 'Oil Pump' in building:
            return 'purple'

    def _set_pos(self, layer=None):

        if layer is None:
            start = -len(self.heads)
            for idx, node in enumerate(self.heads):
                self.pos[node] = (start+(2*idx), -node.depth)
            next_layer = set([node for head in self.heads for node in self.predecessors(head)])
            self._set_pos(next_layer)

        else:
            def _intralayer_pos_key(node):
                sum = 0
                succs = list(self.successors(node))
                for succ in succs:
                    sum += self.pos[succ][0]
                return sum/len(succs)

            layer = sorted(layer, key=_intralayer_pos_key)
            start = -len(layer)
            for idx, node in enumerate(layer):
                self.pos[node] = (start+(2*idx), -node.depth)
            next_layer = set([pred for node in layer for pred in self.predecessors(node)])
            if next_layer:
                self._set_pos(next_layer)

    def show(self):
        #Determine positions of BuildingNodes
        self._set_pos()
        #Create color key
        key = set()
        for node in self:
            key.add(node.building)
        start = -len(key)
        for idx, building in enumerate(key):
            self.add_node(building)
            self.pos[building] = (start+(2*idx), 1)
        #Color all nodes
        cmap = self._get_color_map()
        #Draw
        plt.figure(figsize=(18,10))
        nx.draw(self, with_labels=True, font_size=8, node_color=cmap, pos=self.pos, node_shape='D', node_size=2000)
        plt.show()

if __name__=='__main__':
    pt = ProductTree('Modular Frame', 8)
    pt.show()
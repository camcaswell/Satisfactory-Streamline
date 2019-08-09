class BuildingNode():

    def __init__(self, rec=None, efic=None, depth=None, label=None):
        self.building = rec.building
        self.rec = rec
        self.efic = efic
        self.depth = depth
        if label:
            self.label = label
        elif rec:
            self.label = self.rec.name
        else:
            self.label = None

    def __str__(self):
        if self.efic:
            return f'{self.label}\n{self.efic:.2}'
        else:
            return self.label
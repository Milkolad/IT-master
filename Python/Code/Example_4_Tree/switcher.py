from numpy import unique

class Switcher:
    def convert_to(self, vector):
        uniques = unique(vector).tolist()
        return list(map(lambda x: uniques.index(x), vector))
        
        

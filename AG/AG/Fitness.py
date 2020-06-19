class Fitness:
    def __init__(self, route):
        self.route = route
        self.distance = 0
        self.fitness= 0.0
    
    def routeDistance(self):
        if self.distance ==0:
            chemin_distance = 0
            for i in range(0, len(self.route)):
                ville_depart = self.route[i]
                ville_destination = None
                if i + 1 < len(self.route):
                    ville_destination = self.route[i + 1]
                else:
                    ville_destination = self.route[0]
                chemin_distance += ville_depart.distance(ville_destination)
            self.distance = chemin_distance
        return self.distance
    
    def routeFitness(self):
        if self.fitness == 0:
            self.fitness = 1 / float(self.routeDistance())
        return self.fitness
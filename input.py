import math
import numpy as np

class Input: 
    def creareMatriceSimetricaDistanteDate(self, fisier):   
        f = open(fisier)
        n, _ = [int(x) for x in f.readline().split()]
        D = np.full((n, n), np.inf)
        
        for line in f:
            x, y, d = [float(x) for x in line.split()]
            D[int(x), int(y)] = d
            D[int(y), int(x)] = d
        
        return n, D
    
    def creareMatriceAsimetricaDistanteDate(self, fisier):
        f = open(fisier)
        n, _ = [int(x) for x in f.readline().split()]
        D = np.full((n, n), np.inf)

        for line in f:
            x, y, d = [float(x) for x in line.split()]
            D[int(x), int(y)] = d

        return n, D
    
    def creareMatriceDistanteEuclidieneDate(self, fisier):
        f = open(fisier)
        noduri = []
        for line in f:
            _, x, y = [float(x) for x in line.split()]
            noduri.append([x, y])
        
        n = len(noduri)
        D = np.full((n, n), np.inf)
          
        for i in range(n):
            for j in range(n):
                if i != j:
                    self.D[i, j] = round(math.sqrt( 
                            (noduri[i][0] - noduri[j][0]) * (noduri[i][0] - noduri[j][0]) + \
                                (noduri[i][1] - noduri[j][1]) * (noduri[i][1] - noduri[j][1])
                        ), 4)
                    self.D[j, i] = self.D[i, j]
                
        return n, D
        

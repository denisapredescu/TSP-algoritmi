import heapq
import numpy as np
    
class Branch_and_Bound:
    def __init__(self, n, D):
        self.n = n
        self.D = D
        self.lim = np.inf
        self.drum_optim = None
        self.vizitati = [0] * n 
        self.vecini = self.vecinatate()
        
    def vecinatate(self):
        vecini = [[] for x in range(self.n)]
        for i in range(self.n):
            for j in range(self.n):
                if self.D[i, j] != np.inf:
                    vecini[i].append(j)
        return vecini


    def reducere_matrice(self, Di, i, j, nod_start):
        Dj = Di.copy()
        Dj[i, :] = np.inf          # linia i devine infinit
        Dj[:, j] = np.inf          # coloana j devine infinit  
        Dj[j, nod_start] = np.inf  # distanta de la j la nodul de start devine infinit
        cost = self.f(Dj)          # se calculeaza reducerea
    
        return cost, Dj


    def f(self, Dj):
        n = len(Dj)
        cost = 0                   # costul noii reduceri
        for linie in range(n):
            minim = np.min(Dj[linie, :])
            if minim != 0 and minim != np.inf:
                cost += minim
                Dj[linie, :] -= minim              
        for coloana in range(n):
            minim = np.min(Dj[:, coloana])
            if minim != 0 and minim != np.inf:
                cost += minim
                Dj[:, coloana] -= minim  
        
        return cost
    
    
    def dfs(self, nod, fi, drum, Di):
        self.vizitati[nod] = 1
        
        if fi < self.lim :
            if len(drum) == self.n:
                if self.D[drum[-1], self.nod_start] != np.inf:
                    self.lim = fi
                    self.drum_optim = drum
            else:         
                distante_vecini = []
                for j in self.vecini[nod]:
                    if self.vizitati[j] == 0:  # nodul este fiu nevizitat
                        alfa, Dj = self.reducere_matrice(Di, drum[-1], j)
                        fj = fi + Di[drum[-1], j] + alfa
                        heapq.heappush(distante_vecini, [fj, j, drum + [j], Dj])
                        
                while len(distante_vecini) != 0:
                    fj, nodj, drumj, Dj = heapq.heappop(distante_vecini) 
                    self.dfs(nodj, fj, drumj, Dj)
        
        self.vizitati[nod] = 0  
          
          
    def TSP(self, nod_start = 0):
        self.start = nod_start
        
        Dstart = self.D.copy()
        f_nod_start = self.f(Dstart)
        
        self.dfs(nod_start, f_nod_start, [nod_start], Dstart)

        if self.lim == np.inf:
            return "Nu exista solutie"
        else:
            return self.lim, self.drum_optim

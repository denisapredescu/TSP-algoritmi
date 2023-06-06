import heapq
import random
import numpy as np

class AlgoritmulArboreluiDublu:
    def __init__(self, n, D):
        self.n = n
        self.D = D
        self.ciclu = []
        self.vizitat = np.full(n, 0) 
    
    def prim(self, nod_start):    
        d = np.full(self.n, np.inf)           # distante
        arbore = [[] for _ in range(self.n)]  # lista de adiacenta in care va fi pastrat arborele de cost minim
        vizitat = np.full(self.n, 0)          # vector care tine evidenta daca un nod a fost vizitat 
        h = []                                # coada de prioritati
        d[nod_start] = 0    
        
        # se introduce in coada primul nod si costul drumului pana la acesta
        heapq.heappush(h, [d[nod_start], nod_start, -1])  
        
        for _ in range(self.n):                  
            _, nod, tata = heapq.heappop(h)     
            while vizitat[nod] == 1:
                _, nod, tata =  heapq.heappop(h)  
                
            vizitat[nod] = 1 
            if tata != -1:
                arbore[nod].append(tata)
                arbore[tata].append(nod)
            
            # se pun si vecinii lui nevizitati in coada, daca distanta pana la ei se micsoreaza
            for vecin in range(self.n):           
                if self.D[nod, vecin] != np.inf and vizitat[vecin] == 0 and d[vecin] > self.D[nod, vecin]:  
                    d[vecin] = self.D[nod, vecin]
                    heapq.heappush(h, [d[vecin], vecin, nod])   
        return arbore
    
    # in loc sa se dubleze muchiile si sa se pastreze toate nodurile in care se ajunge,
    # se aplica o parcurgere in adancime si se pastreaza din start doar acelea care nu au fost inca
    # vizitati, imbinand astfel pasii de determinare a ciclului eulerian si aplicarii shortcutting-ului  
    def determinare_ciclu_hamiltonian(self, arbore, k):
        self.parcurgere(k, arbore)
        self.ciclu.append(self.ciclu[0])
        
    def parcurgere(self, i, arbore):
        self.ciclu.append(i)
        self.vizitat[i] = 1
        for j in arbore[i]:         # se parcurg copiii lui i
            if self.vizitat[j] == 0: 
                self.parcurgere(j, arbore)

    def valoare_ciclu(self, ciclu):
        solutie = 0
        for i in range(len(ciclu) - 1):
            solutie += self.D[ciclu[i], ciclu[i + 1]]
            
        return solutie


    def TSP(self):
        nod_start = random.randint(0, self.n - 1)
        arbore = self.prim(nod_start)
        self.determinare_ciclu_hamiltonian(arbore, nod_start)
        solutie = self.valoare_ciclu(self.ciclu)

        return solutie
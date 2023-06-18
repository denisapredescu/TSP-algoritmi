class ProgramareDinamica:
    def __init__(self, n, D):
        self.n = n
        self.D = D
        
    def TSP(self, nod_start = 0):
        # initializare 
        n = self.n
        D = self.D
        V = (1 << n) - 1 # multimea cu toate nodurile
        S = 1 << n       # submultimile (2^n)
        
        # creare matrice M 
        M = [[float('inf')] * n for _ in range(S)]   
        
        # initializarea submultimilor cu 2 noduri cu valorile din matricea de distanta D
        for j in range(1, n):
            M[(1 << j) + (1 << (nod_start))][j] = D[nod_start, j]
    
        # partea recursiva
        for P in range(2, S): # iau toate submultimile
            for j in range(1, n):
                if P & (1 << j) and P & (1 << (nod_start)): # verific sa existe 0 si j in P 
                    for i in range(1, n):
                        # caut i - nod intermediar - care sa nu fie 0 sau j
                        if P & (1 << i) and i != j:         
                            lungime_drum_pana_la_i = M[P ^ (1 << j)][i] + D[i, j]
                            M[P][j] = min(M[P][j], lungime_drum_pana_la_i)
                
        # determinarea solutiei optime
        solutie = float('inf')
        for j in range(n):
            solutie = min(solutie, M[V][j] + D[j, nod_start])
        
        if solutie == float('inf'):
            solutie = "Nu exista solutie" 
                
        return solutie

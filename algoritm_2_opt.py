from euristici_greedy import EuristiciGreedy

class Doi_OPT:
    def __init__(self, n, D):
        self.n = n
        self.D = D

    def calcul_avantaj(self, f, i, j):
        return  self.D[f[i - 1], f[i]] + self.D[f[j - 1], f[j]] - self.D[f[i - 1], f[j - 1]] - self.D[f[i], f[j]]

    def schimburi(self, f, i, j):    
        # creez noul cicul
        # Exemplu: f = abcdef cu i = 2 si j = 4 => g = abdcef
        return f[: i] + f[i : j][::-1] + f[j: ]

    def opt(self, algoritm_determinare_ciclu):
        if algoritm_determinare_ciclu == "farthest-insertion":
            f, solutie = EuristiciGreedy.farthestInsertion(self.n, self.D)
        elif algoritm_determinare_ciclu == "nearest-insertion":
            f, solutie = EuristiciGreedy.nearestInsertion(self.n, self.D)
        elif algoritm_determinare_ciclu == "cheapest-insertion":
            f, solutie = EuristiciGreedy.cheapestInsertion(self.n, self.D)
        elif algoritm_determinare_ciclu == "nearest-neighbor":
            f, solutie = EuristiciGreedy.nearestNeighbor(self.n, self.D)
        else:
            return [], 0
        
        while True:
            avantaj = 0
            g = f
            for i in range(self.n - 2):
                # se porneste de la i + 2 pentru ca nu se face 2-schimb pe 2 muchii care au un nod comun
                for j in range(i + 2, self.n):  
                    # previne incercarea de a face schimb intre 2 muchii cu un nod comun, caz netratat in for loop
                    if i == 0 and j == self.n - 1:   
                        continue 
                    
                    avantaj_g = self.calcul_avantaj(f, i, j)
                    if avantaj_g > avantaj: 
                        g = self.schimburi(f, i, j)
                        avantaj = avantaj_g
            f = g
            solutie -= avantaj
            if avantaj == 0:
                break
    
        return f, solutie
    
    def TSP(self, algoritm_determinare_ciclu="farthest-insertion", repetari = 1):
        solutie_minima = float("inf")

        for _ in range(repetari):
            ciclu, solutie = self.opt(algoritm_determinare_ciclu)
            if solutie < solutie_minima:
                solutie_minima = solutie
                ciclu_solutie_minima = ciclu
          
        return round(solutie_minima, 4), ciclu_solutie_minima

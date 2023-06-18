from euristici_greedy import EuristiciGreedy

# 3 opt inseamna ca se pot face 2 schimburi si 3 schimburi rezultand 7 cicluri
# 3 - 1 modificare de tipul 2-schimburi 
# 3 - 2 modificari de tipul 2 schimburi
# 1 - 3 modificari de tipul 2 schimburi
class Trei_OPT:
    def __init__(self, n, D):
        self.n = n
        self.D = D

    # pentru usuratate se noteaza valorile din f (notat ciclu_f) cu a, b, c, d, e, f
    def calcul_avantaj(self, ciclu_f, i, j, k):
        a = ciclu_f[i - 1]
        b = ciclu_f[i]
        c = ciclu_f[j - 1]
        d = ciclu_f[j]
        e = ciclu_f[k - 1]
        f = ciclu_f[k]
        
        # 1 modificare de tipul 2 - schimburi per ciclu
        # (a, b), (c, d) -> acbdef
        delta_acbdef = self.D[a, b] + self.D[c, d]  - self.D[a, c] - self.D[b, d]
        
        # (a, b), (e, f) ->  aedcbf
        delta_aedcbf = self.D[a, b] + self.D[e, f]  - self.D[a, e] - self.D[b, f]
        
        # (c, d), (e, f) -> abcedf
        delta_abcedf = self.D[c, d] + self.D[e, f]  - self.D[c, e] - self.D[d, f]
        
        # 2 modificari de tipul 2 - schimburi per ciclu
        # (a, b), (c, d), (e, f) -> acbedf
        delta_acbedf = self.D[a, b] + self.D[c, d] + self.D[e, f] - self.D[a, c] - self.D[b, e] - self.D[d, f]
                    
        # (a, b), (c, d), (e, f) -> aedbcf
        delta_aedbcf = self.D[a, b] + self.D[c, d] + self.D[e, f] - self.D[a, e] - self.D[d, b] - self.D[c, f]
        
        # (a, b), (c, d), (e, f) -> adecbf  
        delta_adecbf = self.D[a, b] + self.D[c, d] + self.D[e, f] - self.D[a, d] - self.D[e, c] - self.D[b, f]
        
        # 3 modificari de tipul 2 - schimburi per ciclu
        # (a, b), (c, d), (e, f) -> adebcf
        delta_adebcf = self.D[a, b] + self.D[c, d] + self.D[e, f] - self.D[a, d] - self.D[e, b] - self.D[c, f]
    
        delta_maxim = max([delta_acbdef, delta_aedcbf, delta_abcedf, delta_acbedf, delta_aedbcf, delta_adecbf, delta_adebcf])
        if delta_acbdef == delta_maxim:
            return delta_acbdef, "ij"
        if delta_aedcbf == delta_maxim:
            return delta_aedcbf, "ik"
        if delta_abcedf == delta_maxim:
            return delta_abcedf, "jk"
        if delta_acbedf == delta_maxim:
            return delta_acbedf, "ij-jk"
        if delta_aedbcf == delta_maxim:
            return delta_aedbcf, "ij-ik"
        if delta_adecbf == delta_maxim:
            return delta_adecbf, "jk-ik"
        if delta_adebcf == delta_maxim:
            return delta_adebcf, "ij-jk-ik"


    # metoda foloseste pozitii pentru ca valorile din ciclu se modifica, 
    # motiv pentru care nu mai se poate folosi notatia a, b, c, d, e, f 
    def schimburi(self, f, i, j, k , modificare):
        # 1 modificare de tipul 2 - schimburi per ciclu
        # i, j                
        if modificare == "ij":
            return f[: i] + f[i : j][::-1] + f[j: ] 
        
        # i, k 
        if modificare == "ik":
            return f[: i] + f[i : k][::-1] + f[k: ]

        # j, k
        if modificare == "jk":
            return f[: j] + f[j : k][::-1] + f[k: ]

        # 2 modificari de tipul 2 - schimburi per ciclu
        # i, j -> j, k 
        if modificare == "ij-jk":
            g_ij = f[: i] + f[i : j][::-1] + f[j: ]
            return g_ij[: j] + g_ij[j : k][::-1] + g_ij[k: ]
        
        # i, j -> i, k 
        if modificare == "ij-ik":
            g_ij = f[: i] + f[i : j][::-1] + f[j: ] 
            return g_ij[: i] + g_ij[i : k][::-1] + g_ij[k: ]
        
        # j, k -> i, k
        if modificare == "jk-ik":
            g_jk = f[: j] + f[j : k][::-1] + f[k: ]
            return g_jk[: i] + g_jk[i : k][::-1] + g_jk[k: ]
        
        # 3 modificari de tipul 2 - schimburi per ciclu
        # i, j -> j, k -> i, k
        if modificare == "ij-jk-ik":
            g_ij = f[: i] + f[i : j][::-1] + f[j: ]
            g_ij_jk = g_ij[: j] + g_ij[j : k][::-1] + g_ij[k: ]
            return g_ij_jk[: i] + g_ij_jk[i : k][::-1] + g_ij_jk[k: ]


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
            for i in range(self.n - 4):
                for j in range(i + 2, self.n - 2):
                    for k in range (j + 2, self.n):
                        if i == 0 and k == self.n - 1:
                            continue 
                    
                        avantaj_modificare, modificare = self.calcul_avantaj(f, i, j, k) 
                        if avantaj_modificare > avantaj: 
                            g = self.schimburi(f, i, j, k, modificare)
                            avantaj = avantaj_modificare
            f = g
            solutie -= avantaj  
            if avantaj == 0:
                break
        
        return f, solutie


    def TSP(self, algoritm_determinare_ciclu = "farthest-insertion", repetari = 1):
        solutie_minima = float("inf")

        for _ in range(repetari):
            ciclu, solutie = self.opt(algoritm_determinare_ciclu)
            if solutie < solutie_minima:
                solutie_minima = solutie
                ciclu_solutie_minima = ciclu
          
        return round(solutie_minima, 4), ciclu_solutie_minima
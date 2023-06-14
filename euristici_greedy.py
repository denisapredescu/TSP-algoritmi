import random
import numpy as np 
import heapq

class EuristiciGreedy:
    def farthestInsertion(D, n):
        nod_start = random.randint(0, n - 1)
        h = [0] * n           # lista in cares e retine distanta minima a nodului index fata de ciclu 
        ciclu = [nod_start]   # se insereaza treptat noduri pana cand se ajunge sa aiba lungimea n
        solutie = 0           # calculeaza lungimea ciclului
        vizitat = [0] * n     # retine care nod a fost vizitat 
        vizitat[nod_start] = 1
        
        for i in range(n):
            if i != nod_start:
                h[i] = D[nod_start, i]
            
        while len(ciclu) != n:  
            distanta_maxima = 0
            for nod in range(n):
                if vizitat[nod] == 0 and h[nod] > distanta_maxima:
                    distanta_maxima = h[nod]
                    k = nod

            if len(ciclu) == 1:
                # se creeaza un ciclu cu doua noduri
                ciclu.append(k)
                solutie += 2 * D[ciclu[0], k]
                vizitat[k] = 1
            else: 
                crestere_minima = np.inf
                pozitie_inserare = None
                
                # se iau pe rand numerele din ciclu si se determina pozitia pe care trebuie introdus nodul j
                for i in range(len(ciclu)): 
                    a = ciclu[i]
                    b = ciclu[(i + 1) % len(ciclu)]
                    crestere = D[a, k] + D[k, b] - D[a, b]
                    if crestere < crestere_minima:
                        crestere_minima = crestere
                        pozitie_inserare = i
                        
                ciclu  = ciclu[:pozitie_inserare + 1] + [k] + ciclu[pozitie_inserare + 1:]
                solutie += crestere_minima
                vizitat[k] = 1
                
            for i in range(n):
                if vizitat[i] == 0 and D[k, i] < h[i]:
                    h[i] = D[k, i]     

        return ciclu, solutie


    def nearestInsertion(D, n):
        nod_start = random.randint(0, n - 1)
        h = [0] * n           # lista in cares e retine distanta minima a nodului index fata de ciclu 
        ciclu = [nod_start]   # se insereaza treptat noduri pana cand se ajunge sa aiba lungimea n
        solutie = 0           # calculeaza lungimea ciclului
        vizitat = [0] * n     # retine care nod a fost vizitat 
        vizitat[nod_start] = 1
        
        for i in range(n):
            if i != nod_start:
                h[i] = D[nod_start, i]
        
        while len(ciclu) != n:
            distanta_minima = float('inf')
            for nod in range(n):
                if vizitat[nod] == 0 and h[nod] < distanta_minima:
                    distanta_minima = h[nod]
                    k = nod 
                    
            if len(ciclu) == 1:
                # se creeaza un ciclu cu doua noduri
                ciclu.append(k)
                solutie +=  2 * D[ciclu[0], k]
                vizitat[k] = 1
            else: 
                crestere_minima = np.inf
                pozitie_inserare = None
                
                # se iau pe rand numerele din ciclu si se determina pozitia pe care trebuie introdus nodul j
                for i in range(len(ciclu)): 
                    a = ciclu[i]
                    b = ciclu[(i + 1) % len(ciclu)]
                    crestere = D[a, k] + D[k, b] - D[a, b]
                    if crestere < crestere_minima:
                        crestere_minima = crestere
                        pozitie_inserare = i
                        
                ciclu  = ciclu[:pozitie_inserare + 1] + [k] + ciclu[pozitie_inserare + 1:]
                solutie += crestere_minima
                vizitat[k] = 1
                
            for i in range(n):
                if vizitat[i] == 0 and D[k, i] < h[i]:
                    h[i] = D[k, i]     

        return ciclu, solutie


    def cheapestInsertion(D, n):
        nod_start = random.randint(0, n - 1)
        # lista de prioritati de forma [crestere, pozitie in care ar fi adaugat nodul k, nod k] 
        h = []  
        # se insereaza treptat noduri pana cand se ajunge sa aiba lungimea n
        ciclu = [nod_start]  
        # se retine care nod a fost vizitat 
        vizitat = [0] * n   
        vizitat[nod_start] = 1
        
        # se ia nodul cel mai apropiat de nodul de start k si se insereaza in lista, 
        # formandu-se un ciclu cu cele 2 noduri
        distanta_minima = float("inf")
        for i in range(n):
            if D[nod_start, i] < distanta_minima and nod_start != i:
                distanta_minima = D[nod_start, i]
                k = i 
        ciclu.append(k)                        
        solutie =  2 * D[nod_start, k]  # se calculeaza lungimea ciclului
        vizitat[k] = 1
        
        # introduc cresterile de lungime a distantei care apar daca se introduce orice nod 
        # nevizitata intre cele 2 noduri
        for i in range(n):
            if i != ciclu[0] and i != ciclu[1]:
                crestere = D[ciclu[0], i] + D[i, ciclu[1]] - D[ciclu[0], ciclu[1]]
                heapq.heappush(h, [crestere, 0, i])
    
        while len(ciclu) != n:  
            crestere_minima, pozitie_inserare, k = heapq.heappop(h)
            ciclu = ciclu[:pozitie_inserare + 1] + [k] + ciclu[pozitie_inserare + 1:]
            solutie += crestere_minima
            vizitat[k] = 1
            
            # elimin din coada de prioritati acele calcule care implicau adaugarea unui nod intre i si i + 1
            # pentru ca dupa inserarea lui j, cicu[i + 1] = k, deci acele distante nu mai sunt valide
            # de asemenea, se elimina si tripletele care sugerau ca k este nod are nu face parte din ciclu
            h_aux = []
            
            while len(h) != 0: 
                crestere, pozitie, nod = heapq.heappop(h)
                if pozitie_inserare > pozitie and vizitat[nod] == 0:
                    heapq.heappush(h_aux, [crestere, pozitie, nod])
                if pozitie > pozitie_inserare and vizitat[nod] == 0:
                    heapq.heappush(h_aux, [crestere, (pozitie + 1) % len(ciclu), nod])
    
            h = h_aux
            # trebuie calculete distantele pentru orice nod nevizitat care sa fie inserat
            # intre nodurile ciclu[i] si k, respectiv k si ciclu[i + 2] (k este pe pozitia i + 1)
            for i in range(n):
                if vizitat[i] == 0:
                    a = ciclu[pozitie_inserare]
                    b = ciclu[(pozitie_inserare + 2) % len(ciclu)]
                    heapq.heappush(h, [D[a, i] + D[i, k] - D[a, k], pozitie_inserare, i])   
                    heapq.heappush(h, [D[k, i] + D[i, b] - D[k, b], (pozitie_inserare + 1) % len(ciclu), i])   

        return ciclu, solutie


    def nearestNeighbor(D, n):
        nod_start = random.randint(0, n - 1)   # se alege random nodul de start
        vizitare = [0 for _ in range(n)] 
        vizitare[nod_start] = 1
        ciclu = [nod_start]
        valoare_ciclu = 0                      # suma distantelor care compun ciclul
        
        # cat timp nu s-a creat un ciclu este echivalent cu nu au fost vizitate toate nodurile
        while len(ciclu) != n: 
            # se ia ultimul nod din ciclu si se cauta pentru acesta cel mai apropiat vecin al sau 
            i = ciclu[-1]        
                
            distanta_cel_mai_apropiat_vecin = np.inf
            for j in range(n):
                if i != j and vizitare[j] == 0 and D[i, j] < distanta_cel_mai_apropiat_vecin:
                    distanta_cel_mai_apropiat_vecin = D[i, j]
                    cel_mai_apropiat_vecin = j
            
            # se adauga muchia dintre nodul curent si cel mai apropiat vecin al sau 
            ciclu.append(cel_mai_apropiat_vecin)       
            vizitare[cel_mai_apropiat_vecin] = 1            # se marcheaza ca vizitat
            valoare_ciclu += D[i, cel_mai_apropiat_vecin]   # se adauga valoarea muchiei
        
        # se adauga valoarea muchei de intoarcere in nodul de start
        valoare_ciclu += D[ciclu[n - 1], nod_start]
        
        return ciclu, valoare_ciclu

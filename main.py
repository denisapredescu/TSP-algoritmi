from algoritm_2_opt import Doi_OPT
from algoritm_3_opt import Trei_OPT
from algoritm_christofides import Christofides
from algoritmul_arborelui_dublu import AlgoritmulArboreluiDublu
from branch_and_bound import BranchAndBound
from input import Input
from programare_dinamica import ProgramareDinamica


farthest_insertion = "farthest-insertion"
nearest_insertion = "nearest-insertion"
cheapest_insertion = "cheapest-insertion"
nearest_neighbor = "nearest-neighbor"
greedy_matching = "greedy-matching"
networkX_matching = "networkX-matching"

n, D = Input.creareMatriceDistanteEuclidieneDate("instante/lin105.tsp")

## exemple apel 2-OPT
doi_opt = Doi_OPT(n, D)
solutie, ciclu = doi_opt.TSP(farthest_insertion)
print("Solutie 2-OPT folosind farthest insertion:", solutie)

solutie, ciclu = doi_opt.TSP(nearest_insertion)
print("Solutie 2-OPT folosind nearest insertion:", solutie)

solutie, ciclu = doi_opt.TSP(cheapest_insertion)
print("Solutie 2-OPT folosind cheapest insertion:", solutie)

solutie, ciclu = doi_opt.TSP(nearest_neighbor)
print("Solutie 2-OPT folosind nearest neighbor:", solutie)


## exemple apel 3-OPT
trei_opt = Trei_OPT(n, D)
solutie, ciclu = trei_opt.TSP(farthest_insertion)
print("Solutie 3-OPT folosind farthest insertion:", solutie)

solutie, ciclu = trei_opt.TSP(nearest_insertion)
print("Solutie 3-OPT folosind nearest insertion:", solutie)

solutie, ciclu = trei_opt.TSP(cheapest_insertion)
print("Solutie 3-OPT folosind cheapest insertion:", solutie)

solutie, ciclu = trei_opt.TSP(nearest_neighbor)
print("Solutie 3-OPT folosind nearest neighbor:", solutie)


## exemple apel algoritmul lui Christofides
christofides = Christofides(n, D)
solutie, ciclu = christofides.TSP(greedy_matching, 10)
print("Solutie Christofides varianta in care cuplajul e realizat folosind o strategie greedy:", solutie)

solutie_fathest = christofides.TSP(networkX_matching)
print("Solutie Christofides:", solutie)


## exemple apel algoritmul arborelui dublu
arbore_dublu = AlgoritmulArboreluiDublu(n, D)
solutie, ciclu = doi_opt.TSP()
print("Solutie algoritm arborelui dublu:", solutie)


## exemple apel algoritm ce are la baza programare dinamica
n, D = Input.creareMatriceAsimetricaDistanteDate("instante/grader_test20.in")
programare_dinamica = ProgramareDinamica(n, D)
solutie = programare_dinamica.TSP()
print("Solutie Programare Dinamica:", solutie)


## exemple apel algoritm ce are la baza programare dinamica
doi_opt = BranchAndBound(n, D)
solutie, ciclu = doi_opt.TSP()
print("Solutie Branch and bound:", solutie)
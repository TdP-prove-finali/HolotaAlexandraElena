from model.model import Model

mymodel = Model()

mymodel.buildGrafo(1,38000000, 242)

n, a = mymodel.getGraphDetails()
print(f"Nodi: {n} - Archi: {a}")

mymodel.getBestNodes()
print(f"{mymodel.bestScore}")

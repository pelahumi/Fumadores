from Fumadores import *

def lanzador():
    #Creamos un fumador por ingrediente
    fumadores = [Fumador(ingrediente) for ingrediente in INGREDIENTES]

    #Creamos el agente
    agente = Agente()

    #Iniciamos
    for fumador in fumadores:
        fumador.start()
    agente.start()
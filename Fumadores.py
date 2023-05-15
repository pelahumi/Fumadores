import threading
import random
import time

#Creamos una lista con los ingredientes
INGREDIENTES = ["papel", "tabaco", "filtros", "green", "cerillas"]

#Condiciones
puede_fumar = threading.Condition()
disponible = threading.Condition()

#Clase fumador
class Fumador(threading.Thread):
    def __init__(self, ingrediente):
        super().__init__(self)
        self.ingrediente = ingrediente
    
    def run(self):
        while True:
            with puede_fumar:
                puede_fumar.wait()
                if self.ingrediente in INGREDIENTES:
                    print("Fumador con ",self.ingrediente, "cogió el resto y está fumando.")
                    time.sleep(2.5)
                    puede_fumar.notify()

#Clase agente
class Agente(threading.Thread):
    def __init__(self):
        super().__init__(self)
    
    def run(self):
        while True:
            with disponible:
                ingrediente1, ingrediente2 = random.sample(INGREDIENTES, 2)
                print("El agente colocó ",ingrediente1, "y", ingrediente2, "en la mesa.")
                with puede_fumar:
                    puede_fumar.notify_all()
                time.sleep(1)
                with puede_fumar:
                    puede_fumar.wait()
                
            
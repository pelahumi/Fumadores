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
            
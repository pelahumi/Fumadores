# Fumadores
Pincha [aquí](https://github.com/pelahumi/Fumadores) para acceder a mi repositorio.

## Índice
  - [Resumen](#1)
  - [Código y explicación](#2)
  - [Output](#3)
  
---

## Resumen<a name="1"></a>

La idea de este trabajo era dar una solución al problema de los fumadores. En el cual un grupo de fumadores quieren fumar, pero cada uno tiene un ingrediente necesario para hacer el ciagarrillo (papel, tabaco, filtros, green y cerillas), menos uno, el agente, que tiene todos los ingredientes. La idea es que el agente deje todos los ingredientes en la mesa y que un fumadorlos coja. Una vez acabe de hacer su cigarrillo los deje en la mesa y los coja el siguiente.

---

## Código y explicación<a name="2"></a>

Importamos las librerías que vamos a utilizar:

```
import threading
import time
import random
```

Creamos una lista invariable con todos los ingredientes necesarios para hacer un cigarrillo:

```
INGREDIENTES = ["papel", "tabaco", "filtros", "green", "cerillas"]
```

A continuación, creamos las condiciones para bloquear y desbloquear el acceso a los recursos:

```
puede_fumar = threading.Condition()
disponible = threading.Condition()
```

Creamos la clase ```Fumador()```, al que le añadimos un atributo, su ingrediente:

```
class Fumador(threading.Thread):
    def __init__(self, ingrediente):
        super().__init__()
        self.ingrediente = ingrediente
```

El método ```run()``` simplemente ejecutará la acción para que cada fumador pueda fumar. Los fumadores esperan hasta que el que está fumando acabe de fumar.

```
    def run(self):
        while True:
            with puede_fumar:
                puede_fumar.wait()
                if self.ingrediente in INGREDIENTES:
                    print("Fumador con ",self.ingrediente, "cogió el resto y está fumando.")
                    time.sleep(2.5)
                    puede_fumar.notify()
```

Creamos la clase ```Agente()```:

```
class Agente(threading.Thread):
    def __init__(self):
        super().__init__()
```

Le añadimos el método ```run()```, en el que el agente deja 4 de los 5 ingredientes en la mesa, y el que tiene el ingrediente que falta puede fumar:

```
    def run(self):
        while True:
            with disponible:
                ingrediente1, ingrediente2, ingrediente3, ingrediente4 = random.sample(INGREDIENTES, 4)
                print("El agente colocó ",ingrediente1, ",", ingrediente2,",", ingrediente3, "y", ingrediente4, "en la mesa.")
                with puede_fumar:
                    puede_fumar.notify_all()
                time.sleep(1)
                with puede_fumar:
                    puede_fumar.wait()
```

Por último creamos otro archivo en el que crearemos una función para ejecutar todo el código. La función ```lanzador()``` crea tantos fumadores como ingredientes y los guarda en una lista. Se crea un objeto agente. Y ejecuta todos los hilos con la función ```.start()```:

```
def lanzador():
    fumadores = [Fumador(ingrediente) for ingrediente in INGREDIENTES]

    agente = Agente()

    for fumador in fumadores:
        fumador.start()
    agente.start()
``` 

---

## Ouput<a name="3"></a>
El ouput del código es el siguiente:

<img width="475" alt="Captura de pantalla 2023-05-16 a las 11 24 01" src="https://github.com/pelahumi/Fumadores/assets/91721764/f6e7490d-863c-42f6-ac01-e4ea3bb37575">




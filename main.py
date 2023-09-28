import models 
from models import *
import constantes 
from constantes import *

# En este archivo lo que vamos a tener es el flujo de combate.
# es el que ira generando turnos de combate a medida que se van eligiendo los ataques que se realizaran.

pokemon1 = Pokemon("Bulbasaur", 100, "Grass", "poison")

pokemon2 = Pokemon("Charmander", 100, "Fire", None)

# Stats

pokemon1.stats = {
    HP: 45,
    ATTACK: 49,
    DEFENSE: 49,
    SPATTACK: 65,
    SPDEFENSE: 65,
    SPEED: 45,
}



pokemon2.stats = {
    HP: 39,
    ATTACK: 52,
    DEFENSE: 43,
    SPATTACK: 80,
    SPDEFENSE: 65,
    SPEED: 65,
}



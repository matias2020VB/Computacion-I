import models 
from models import *
import constantes 
from constantes import *

# En este archivo lo que vamos a tener es el flujo de combate.
# es el que ira generando turnos de combate a medida que se van eligiendo los ataques que se realizaran.

pokemon1 = Pokemon("Bulbasaur", 100, "Grass", "poison")
pokemon2 = Pokemon("Charmander", 100, "Fire", None)

pokemon1.current_hp = 45
pokemon2.current_hp = 39


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

# Accedemos al vector de ataques.

pokemon1.attacks = [Attack("Scratch", "normal", PHYSICAL, 10, 10, 100)]
pokemon2.attacks = [Attack("Blaze", "normal", PHYSICAL, 10, 10, 100)]

# Start battle -> Instanciamos un objeto de la clase batalla que recibira a bulbasaur y a charmander

battle = Battle(pokemon1, pokemon2)

# Mientras la batalla no esté terminada
# Tendremos que definir la clase comando pa


# Esta funcion que nos permitira las instrucciones para cada pokemon.
def ask_command(pokemon):
    command = None
    while not command:
        # DO ATTACK -> attack 0 # -> ataco con el primer ataque del vector de ataques del pokemon ¿Como valido este input?
        tmp_command = input("Que deberia hacer el: " + pokemon.name).split(" ") # -> Que deberia hacer el pokemon en caso de que no haya un comando indicado por parte del usuario.
        if len(tmp_command) == 2:
            try:
                if tmp_command[0] == DO_ATTACK and 0 <= int(tmp_command[1]) < 4:
                    command = command({DO_ATTACK: int(tmp_command[1])})
            except Exception:
                pass            
    return command



while not battle.is_finished(pokemon1):
    command1 = ask_command(pokemon1)
    command2 = ask_command(pokemon2)
    
    
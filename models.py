class PokemonCharacter():
    def __init__(self, name, level, type1, type2):
        self.name = name
        self.level = level
        self.type1 = type1
        self.type2 = type2
        self.attacks = [] # Vector de ataques, numero arbitrario de ataques. Limitacion a 4 ataques. necesitamos que contenga los objetos de ataques pokemon
        self.stats = {}
        self.current_status = 0 # Control de estados: Envenenamiento, quemaduras, paralizado etc.
        self.current_hp = 0 # Vida actual del pokemon, luego de recibir un ataque variará.
              
class Attack():
    def __init__(self, name, type_Atk, category, power, accurracy, pp):
        self.name = name
        self.type_Atk = type_Atk
        self.category = category
        self.power = power
        self.catergory = category
        self.pp = pp

class Battle():
    def __init__(self, pokemon1, pokemon2):
        self.pokemon1 = pokemon1 # Mi pokemon
        self.pokemon2 = pokemon2 # Pokemon enemigo
        self.actual_turn = 0 # Nos mostrara que turno estamos en el combate.

    def is_finished(self): 
#   ¿Cuando se termina un combate pokemon?
#   Se termina cuando uno de los dos pokemones tiene 0 puntos de salud o pueden ser negativos considerando que algunos ataques pueden dejar
#   En vida negativa (dependiendo del daño)
        return self.pokemon1.current_hp <= 0 or self.pokemon2.current_hp <= 0  
    
    
   
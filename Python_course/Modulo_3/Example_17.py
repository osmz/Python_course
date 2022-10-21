# Ash Ketchum, el personaje principal del anime Pokémon, está a punto de luchar en la final de la liga Kalos. En estos eventos compiten los mejores entrenadores del mundo en batallas donde cada entrenador puede tener 3, 4, 5 o 6 criaturas. Ash quiere saber, para una cantidad de criaturas específica, si él podrá formar un equipo únicamente con Pokémon seudolegendarios para competir en la final. Un pokemon seudolegendario es aquel que en la suma de sus estadísticas de combate tiene 600 puntos o más.

# Las estadísticas de combate de cada pokemon son 6:  
 
# "ataque"
 
# "defensa"
 
# "ataque_especial"
 
# "defensa_especial"
 
# "velocidad"
 
# "vida"  
 
# Escriba una función que, dada una lista de diccionarios (cada uno representando un pokémon) con las anteriores estadísticas, determine si Ash podrá formar un equipo de pokémon seudolegendarios para afrontar la final de la liga. En caso que Ash pueda formar un equipo, retorne una lista con los nombres de las criaturas que Ash utilizaría en la batalla. Si es imposible generar un equipo que cumpla con las condiciones, retorne None.
 
# Se garantiza que en caso de poder formar un equipo válido, solamente habrá una configuración posible.  
 
# La lista de retorno debe componerse únicamente de cadenas de caracteres y debe tener el mismo orden de la lista que llega por parámetro.  

def construir_equipo_pokemon(Cantidad, Lista_pkmn):
    equipo = []
    equipo_seudolegendarios = False

    if Cantidad >= 3:
        for criatura in Lista_pkmn:
            puntos_combate = criatura['ataque'] + criatura['defensa'] + criatura['ataque_especial'] + criatura['defensa_especial'] + criatura['velocidad'] + criatura['vida']
            print(puntos_combate)

            if puntos_combate >= 600:
                dic_equipo = criatura['nombre']
                equipo.append(dic_equipo)
                equipo_seudolegendarios = True
    else:
        equipo = None

    if Cantidad != len(equipo):
        equipo = None

    if equipo_seudolegendarios == False:
        equipo = None
    
    return equipo

print(construir_equipo_pokemon(5, [{'nombre': 'Rayquaza', 'vida': 100, 'ataque': 100, 'defensa': 100, 'ataque_especial': 100, 'defensa_especial': 100, 'velocidad': 100}, {'nombre': 'Pikachu', 'vida': 100, 'ataque': 1001, 'defensa': 100, 'ataque_especial': 100, 'defensa_especial': 1, 'velocidad': 1}]))       

print(construir_equipo_pokemon(4, [{'nombre': 'Rayquaza', 'vida': 120, 'ataque': 120, 'defensa': 120, 'ataque_especial': 120, 'defensa_especial': 120, 'velocidad': 120}, {'nombre': 'Arceus', 'vida': 120, 'ataque': 120, 'defensa': 120, 'ataque_especial': 120, 'defensa_especial': 120, 'velocidad': 120}, {'nombre': 'Solgaleo', 'vida': 100, 'ataque': 100, 'defensa': 100, 'ataque_especial': 200, 'defensa_especial': 100, 'velocidad': 100}, {'nombre': 'Charizard-X', 'vida': 100, 'ataque': 100, 'defensa': 100, 'ataque_especial': 50, 'defensa_especial': 50, 'velocidad': 100}, {'nombre': 'Greninja', 'vida': 100, 'ataque': 100, 'defensa': 100, 'ataque_especial': 100, 'defensa_especial': 100, 'velocidad': 100}, {'nombre': 'Swellow', 'vida': 60, 'ataque': 80, 'defensa': 50, 'ataque_especial': 70, 'defensa_especial': 60, 'velocidad': 150}, {'nombre': 'Pikachu', 'vida': 20, 'ataque': 20, 'defensa': 20, 'ataque_especial': 20, 'defensa_especial': 20, 'velocidad': 20}]))       
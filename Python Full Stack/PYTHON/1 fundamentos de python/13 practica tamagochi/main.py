from persona import Persona
from tamagotchi import Tamagotchi

# Crear una instancia de Tamagotchi
mi_tamagotchi = Tamagotchi(nombre="Tama", color="Azul")

# Crear una instancia de Persona con el Tamagotchi
persona = Persona(nombre="Juan", apellido="Pérez", tamagotchi=mi_tamagotchi)

# Interacciones
persona.darle_comida()  # Darle de comer al tamagotchi
persona.jugar_con_tamagotchi()  # Jugar con el tamagotchi
persona.curarlo()  # Curar al tamagotchi






from persona import Persona
from tamagotchi_feliz import TamagotchiFeliz

# Crear una instancia de TamagotchiFeliz
mi_tamagotchi_feliz = TamagotchiFeliz(nombre="Tami", color="Verde")

# Crear una instancia de Persona con el TamagotchiFeliz
persona = Persona(nombre="Ana", apellido="López", tamagotchi=mi_tamagotchi_feliz)

# Interacciones
persona.jugar_con_tamagotchi()  # Observa el comportamiento especial de TamagotchiFeliz

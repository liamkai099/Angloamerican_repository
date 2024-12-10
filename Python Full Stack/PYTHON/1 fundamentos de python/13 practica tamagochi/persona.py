# Importamos la clase Tamagotchi desde tamagotchi.py
from tamagotchi import Tamagotchi

# Clase Persona
class Persona:
    def __init__(self, nombre, apellido, tamagotchi):
        self.nombre = nombre
        self.apellido = apellido
        self.tamagotchi = tamagotchi

    def jugar_con_tamagotchi(self):
        print(f"{self.nombre} está jugando con {self.tamagotchi.nombre}.")
        self.tamagotchi.jugar()

    def darle_comida(self):
        print(f"{self.nombre} le está dando comida a {self.tamagotchi.nombre}.")
        self.tamagotchi.comer()

    def curarlo(self):
        print(f"{self.nombre} está curando a {self.tamagotchi.nombre}.")
        self.tamagotchi.curar()

from tamagotchi import Tamagotchi

class TamagotchiFeliz(Tamagotchi):
    def __init__(self, nombre, color):
        super().__init__(nombre, color)
        self.felicidad += 20  # Este tipo de Tamagotchi comienza con más felicidad

    def jugar(self):
        super().jugar()
        print(f"{self.nombre} está más feliz de lo normal!")

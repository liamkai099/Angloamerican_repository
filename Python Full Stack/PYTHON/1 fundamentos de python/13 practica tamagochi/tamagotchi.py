# Clase Tamagotchi
class Tamagotchi:
                # Atributos o propiedades de instancia (objetos)
    def __init__(self, nombre, color, salud=100, felicidad=50, energia=50):
        self.nombre = nombre      # inicializamos los atributos de instancia
        self.color = color
        self.salud = salud
        self.felicidad = felicidad
        self.energia = energia

# creamos los metodos de instancia 
    def jugar(self):
        # Incrementa felicidad, reduce salud
        self.felicidad += 10
        self.salud -= 5
        print(f"{self.nombre} está jugando. Felicidad: {self.felicidad}, Salud: {self.salud}")

    def comer(self):
        # Incrementa felicidad y salud
        self.felicidad += 5
        self.salud += 10
        print(f"{self.nombre} está comiendo. Felicidad: {self.felicidad}, Salud: {self.salud}")

    def curar(self):
        # Incrementa salud, reduce felicidad
        self.salud += 20
        self.felicidad -= 5
        print(f"{self.nombre} está siendo curado. Salud: {self.salud}, Felicidad: {self.felicidad}")

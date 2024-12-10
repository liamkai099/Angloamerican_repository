"""
Definición de una clase
Una clase se define utilizando la palabra clave class, seguida del nombre de la clase y dos puntos (:).
Dentro de la clase, puedes definir atributos y métodos.
"""

class Usuario:

    # Atributos o propiedades de la instancio (o objetos)
    def __init__(self, nombre, apellido, email): 

        """
        init__: Es el constructor de la clase. Se ejecuta cuando se crea un objeto. Aquí es donde se inicializan 
        los atributos del objeto.
        El constructor __init__
        En Python, cada vez que creamos un objeto a partir de una clase, el método especial __init__ se ejecuta automáticamente. 
        Este método se utiliza para inicializar los atributos de la clase con los valores que le pasamos cuando creamos el objeto.

        self: Es una referencia al propio objeto. Es un parámetro que deben tener todos los métodos de
        una clase, y nos permite acceder a los atributos y métodos del objeto.
        """

# inicializamos los atributos de instancia
        self.nombre = nombre

        self.apellido = apellido   

        self.email = email

        self.limite_credito = 30000

        self.saldo_pagar = 0

        """
        Métodos de instancia y métodos de clase:
        _______________________________________

        Métodos de instancia: Son los métodos normales de una clase, que operan sobre los atributos 
        de una instancia (es decir, sobre el objeto específico). Reciben como primer parámetro self.

        Métodos de clase: Son métodos que operan sobre la clase misma, no sobre las instancias.
        Para definir un método de clase, se utiliza el decorador @classmethod y recibe como primer 
        parámetro cls, que hace referencia a la clase.
        """



# creamos un metodos de instancia (Métodos de instancia)

    def hacer_compra(self, monto):  #recibe como argumento el monto de la compra

        self.saldo_pagar += monto   #el saldo a pagar del usuario aumenta en la cantidad del valor recibido
        return self



    def pagar_tarjeta(self,monto):
        self.saldo_pagar -= monto   #el saldo a pagar del usuario aumenta en la cantidad del valor recibido
        return self



    def mostrar_saldo_usuario(self):
        print(f"usuario: {self.nombre}, saldo a pagar: ${self.saldo_pagar}")
        return self



    def transferir_deuda(self):
        pass



usuario1 = Usuario("a","b","c")

Usuario2 = Usuario("d","f","h")

Usuario3 = Usuario("j","k","l")


usuario1.hacer_compra(1000).hacer_compra(2000)
print(usuario1.saldo_pagar)
usuario1.pagar_tarjeta(1000)
print(usuario1.saldo_pagar)
usuario1.mostrar_saldo_usuario


























class Usuario:

    def __init__(self, nombre, apellido, email):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.limite_credito = 30000
        self.saldo_pagar = 0

    def hacer_compra(self, monto):
        """Aumenta el saldo a pagar con el monto de la compra."""
        self.saldo_pagar += monto

    def pagar_tarjeta(self, monto):
        """Reduce el saldo a pagar según el monto que se pague."""
        if monto > self.saldo_pagar:
            print(f"El monto a pagar ({monto}) es mayor que el saldo actual ({self.saldo_pagar}). No se puede procesar.")
        else:
            self.saldo_pagar -= monto

    def mostrar_saldo_usuario(self):
        """Muestra el saldo pendiente a pagar del usuario."""
        return f"El saldo a pagar de {self.nombre} {self.apellido} es: ${self.saldo_pagar}"
    
    def transferir_deuda(self, otro_usuario, monto):
        """Transfiere parte de la deuda de este usuario a otro usuario."""
        if monto > self.saldo_pagar:
            print(f"El monto a transferir ({monto}) es mayor que el saldo a pagar ({self.saldo_pagar}). No se puede realizar la transferencia.")
        else:
            self.saldo_pagar -= monto
            otro_usuario.saldo_pagar += monto
            print(f"{self.nombre} {self.apellido} ha transferido ${monto} a {otro_usuario.nombre} {otro_usuario.apellido}.")


# Crear instancias de Usuario
usuario1 = Usuario("Juan", "Pérez", "juan.perez@email.com")
usuario2 = Usuario("Ana", "Gómez", "ana.gomez@email.com")
usuario3 = Usuario("Carlos", "Rodríguez", "carlos.rodriguez@email.com")

# Usuario 1: Hace 2 compras y luego paga su tarjeta.
usuario1.hacer_compra(5000)
usuario1.hacer_compra(7000)
usuario1.pagar_tarjeta(9000)
print(usuario1.mostrar_saldo_usuario())

# Usuario 2: Hace 1 compra y luego paga 2 veces su tarjeta.
usuario2.hacer_compra(12000)
usuario2.pagar_tarjeta(5000)
usuario2.pagar_tarjeta(3000)
print(usuario2.mostrar_saldo_usuario())

# Usuario 3: Hace 3 compras y luego paga su tarjeta 4 veces.
usuario3.hacer_compra(4000)
usuario3.hacer_compra(3000)
usuario3.hacer_compra(6000)
usuario3.pagar_tarjeta(3000)
usuario3.pagar_tarjeta(2000)
usuario3.pagar_tarjeta(2000)
usuario3.pagar_tarjeta(1500)
print(usuario3.mostrar_saldo_usuario())

# Transferir deuda de usuario3 a usuario1
usuario3.transferir_deuda(usuario1, 2000)
print(usuario1.mostrar_saldo_usuario())
print(usuario3.mostrar_saldo_usuario())
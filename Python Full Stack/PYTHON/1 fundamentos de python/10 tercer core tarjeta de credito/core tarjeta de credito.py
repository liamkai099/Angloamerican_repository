class TarjetaCredito:
    
    # Atributo de clase para almacenar todas las instancias de tarjetas
    lista_tarjetas = []

    # Método constructor con valores por default
    def __init__(self, saldo_pagar=0.0, limite_credito=0.0, intereses=0.0):
        # Inicializando los atributos de la tarjeta
        self.saldo_pagar = saldo_pagar
        self.limite_credito = limite_credito
        self.intereses = intereses
        # Al crear una nueva tarjeta, la agregamos a la lista de tarjetas
        TarjetaCredito.lista_tarjetas.append(self)

    # Método para hacer compras, aumenta el saldo si no se excede el límite de crédito
    def compra(self, monto):
        if self.saldo_pagar + monto > self.limite_credito:
            print("Tarjeta Rechazada, has alcanzado tu límite de crédito")
        else:
            self.saldo_pagar += monto
        return self  # Para poder encadenar llamadas

    # Método para hacer pagos, disminuye el saldo a pagar
    def pago(self, monto):
        self.saldo_pagar -= monto
        if self.saldo_pagar < 0:
            self.saldo_pagar = 0  # Evita que el saldo sea negativo
        return self  # Para poder encadenar llamadas

    # Método para mostrar el saldo a pagar
    def mostrar_info_tarjeta(self):
        print(f"Saldo a Pagar: ${self.saldo_pagar:.2f}")

    # Método para cobrar intereses sobre el saldo
    def cobrar_interes(self):
        self.saldo_pagar += self.saldo_pagar * self.intereses
        return self  # Para poder encadenar llamadas

    # Método de clase para imprimir la información de todas las tarjetas creadas
    @classmethod
    def mostrar_todas_las_tarjetas(cls):
        for tarjeta in cls.lista_tarjetas:
            tarjeta.mostrar_info_tarjeta()


# Creando instancias de la tarjeta con valores específicos
tarjeta1 = TarjetaCredito(1000, 3000, 0.02)  # Saldo 1000, Límite 500, Interés 2%
tarjeta2 = TarjetaCredito(2000, 3000, 0.05)  # Saldo 5000, Límite 1000, Interés 5%
tarjeta3 = TarjetaCredito(2000, 3000, 0.1)   # Saldo 2000, Límite 300, Interés 10%

# Realizando operaciones en las tarjetas y encadenando los métodos para la tarjeta 1
tarjeta1.compra(50).compra(100).pago(30).cobrar_interes().mostrar_info_tarjeta()

# Realizando operaciones en las tarjetas y encadenando los métodos para la tarjeta 2
tarjeta2.compra(200).compra(150).compra(100).pago(50).pago(20).cobrar_interes().mostrar_info_tarjeta()

# Realizando operaciones en las tarjetas y excediendo el límite para la tarjeta 3
tarjeta3.compra(500).compra(500).compra(500).compra(1000).compra(500).compra(500).mostrar_info_tarjeta()

# Bonus: Mostrar la información de todas las tarjetas creadas
TarjetaCredito.mostrar_todas_las_tarjetas()


"""
1 Crea la clase TarjetaCredito con los atributos de saldo_pagar, limite_credito, intereses  xxx

2 Crea el método compra para la clase TarjetaCredito   xxx

3 Crea el método pago para la clase TarjetaCredito   xxx

4 Crea el método mostrar_info_tarjeta para la clase TarjetaCredito xxx

5 Crea el método cobrar_interes para la clase TarjetaCredito xxx

6 Crea 3 tarjetas  xxx

7 Para la primera tarjeta, haz 2 compras y un pago. Luego cobra los intereses y muestra la xxx
información de la tarjeta; todo esto en una sola línea a través de la encadenación.

8 Para la segunda tarjeta, haz 3 compras y 2 pagos. Luego cobra los intereses y muestra la xxx
información de la tarjeta; todo esto en una sola línea a través de la encadenación.

9 Para la tercera tarjeta, haz 5 compras y excede su límite de crédito. Luego muestra la  xxx
información de la tarjeta; todo esto en una sola línea a través de la encadenación.

10 BONUS: crea un método de clase para imprimir todas las instancias de la información
de las tarjetas creadas. En el capítulo pasado te dimos algunas pistas de cómo realizarlo.
"""
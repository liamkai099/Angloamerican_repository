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


from tarjetacredito import TarjetaCredito  # Asegúrate de importar la clase TarjetaCredito

class Usuario:

    def __init__(self, nombre, apellido, email):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        # Lista de tarjetas de crédito asociadas al usuario (permite múltiples tarjetas)
        self.tarjetas = [TarjetaCredito(0, 20000, 0.015)]  # Asignamos una tarjeta de crédito por defecto

    def hacer_compra(self, monto, tarjeta_index=0):
        """
        Aumenta el saldo a pagar con el monto de la compra en una tarjeta específica.
        Si no se especifica la tarjeta, se usa la primera en la lista (tarjeta_index=0).
        """
        if tarjeta_index < len(self.tarjetas):
            tarjeta = self.tarjetas[tarjeta_index]
            tarjeta.compra(monto)
        else:
            print(f"No existe una tarjeta con el índice {tarjeta_index}.")

    def pagar_tarjeta(self, monto, tarjeta_index=0):
        """
        Reduce el saldo a pagar según el monto que se pague en una tarjeta específica.
        Si no se especifica la tarjeta, se usa la primera en la lista (tarjeta_index=0).
        """
        if tarjeta_index < len(self.tarjetas):
            tarjeta = self.tarjetas[tarjeta_index]
            tarjeta.pago(monto)
        else:
            print(f"No existe una tarjeta con el índice {tarjeta_index}.")

    def mostrar_saldo_usuario(self):
        """
        Muestra el saldo pendiente a pagar de todas las tarjetas del usuario.
        """
        for i, tarjeta in enumerate(self.tarjetas):
            print(f"Saldo pendiente de la tarjeta {i+1}: ${tarjeta.saldo_pagar:.2f}")

    def agregar_tarjeta(self, saldo_inicial=0, limite_credito=20000, intereses=0.015):
        """
        Permite agregar una nueva tarjeta de crédito al usuario.
        """
        nueva_tarjeta = TarjetaCredito(saldo_inicial, limite_credito, intereses)
        self.tarjetas.append(nueva_tarjeta)
        print(f"Se ha agregado una nueva tarjeta con límite de crédito de ${limite_credito}.")

    def transferir_deuda(self, monto, tarjeta_origen_index=0, tarjeta_destino_index=1):
        """
        Transfiere parte de la deuda de una tarjeta a otra dentro del mismo usuario.
        """
        if tarjeta_origen_index < len(self.tarjetas) and tarjeta_destino_index < len(self.tarjetas):
            tarjeta_origen = self.tarjetas[tarjeta_origen_index]
            tarjeta_destino = self.tarjetas[tarjeta_destino_index]

            if monto > tarjeta_origen.saldo_pagar:
                print(f"El monto a transferir ({monto}) es mayor que el saldo a pagar ({tarjeta_origen.saldo_pagar}). No se puede realizar la transferencia.")
            else:
                tarjeta_origen.saldo_pagar -= monto
                tarjeta_destino.saldo_pagar += monto
                print(f"Se han transferido ${monto} de la tarjeta {tarjeta_origen_index+1} a la tarjeta {tarjeta_destino_index+1}.")
        else:
            print(f"Una de las tarjetas especificadas no existe.")








# ejemplos:


# Crear un usuario
usuario = Usuario("Juan", "Pérez", "juan@example.com")

# Mostrar saldo inicial
usuario.mostrar_saldo_usuario()

# Hacer compras con la primera tarjeta
usuario.hacer_compra(500)  # Compra en la primera tarjeta
usuario.hacer_compra(1000, tarjeta_index=0)  # Otra compra en la primera tarjeta

# Mostrar saldo después de las compras
usuario.mostrar_saldo_usuario()

# Agregar una nueva tarjeta
usuario.agregar_tarjeta(saldo_inicial=1000, limite_credito=30000, intereses=0.02)

# Mostrar saldo después de agregar una nueva tarjeta
usuario.mostrar_saldo_usuario()

# Hacer una compra en la segunda tarjeta
usuario.hacer_compra(200, tarjeta_index=1)

# Mostrar saldo después de la compra en la nueva tarjeta
usuario.mostrar_saldo_usuario()

# Transferir deuda entre tarjetas
usuario.transferir_deuda(500, tarjeta_origen_index=0, tarjeta_destino_index=1)

# Mostrar saldo después de la transferencia de deuda
usuario.mostrar_saldo_usuario()





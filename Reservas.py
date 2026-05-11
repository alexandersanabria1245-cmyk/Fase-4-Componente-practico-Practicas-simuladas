Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> """
... Clase Reserva: integra cliente, servicio, duración y estado.
... """
... from excepciones import ReservaError, ServicioNoDisponibleError
... from logger import registrar_log
... from entidades import Cliente
... from servicios import Servicio
... 
... class Reserva:
...     ESTADOS = ["PENDIENTE", "CONFIRMADA", "CANCELADA"]
... 
...     def __init__(self, cliente: Cliente, servicio: Servicio, duracion: int):
...         self.cliente = cliente
...         self.servicio = servicio
...         self.duracion = duracion
...         self.estado = "PENDIENTE"
...         # Validación automática del cliente y parámetros básicos
...         cliente.validar()
...         if duracion <= 0:
...             raise ReservaError("La duración debe ser mayor a cero.")
...         registrar_log(f"Reserva creada: {cliente.identificador} -> {servicio.identificador} ({duracion}h)")
... 
...     def confirmar(self, **kwargs) -> bool:
...         """Confirma la reserva previa validación del servicio."""
...         try:
...             self.servicio.validar_parametros(**kwargs)
...             if self.estado != "PENDIENTE":
...                 raise ReservaError(f"No se puede confirmar una reserva en estado {self.estado}.")
...             self.estado = "CONFIRMADA"
...             registrar_log(f"Reserva {self.cliente.identificador}-{self.servicio.identificador} CONFIRMADA.")
...             return True
...         except ServicioNoDisponibleError as e:
...             registrar_log(f"Error al confirmar: {e}", nivel="ERROR")
...             raise ReservaError("No se pudo confirmar la reserva.") from e

    def cancelar(self) -> bool:
        """Cancela la reserva si aún no ha sido cancelada."""
        try:
            if self.estado == "CANCELADA":
                raise ReservaError("La reserva ya está cancelada.")
            self.estado = "CANCELADA"
            registrar_log(f"Reserva {self.cliente.identificador}-{self.servicio.identificador} CANCELADA.")
            return True
        except ReservaError as e:
            registrar_log(f"Error al cancelar: {e}", nivel="ERROR")
            raise

    def procesar(self, **kwargs) -> float:
        """
        Procesa la reserva: confirma si no lo está y calcula el costo.
        Retorna el costo total.
        """
        try:
            if self.estado != "CONFIRMADA":
                self.confirmar(**kwargs)  # Encadenamiento natural si falla
            # Ahora calcular costo
            costo = self.servicio.calcular_costo(self.duracion, **kwargs)
            registrar_log(f"Reserva procesada: costo ${costo:.2f}")
            return costo
        except Exception as e:
            registrar_log(f"Error procesando reserva: {e}", nivel="ERROR")
            raise ReservaError("Error durante el procesamiento de la reserva.") from e

    def __str__(self):

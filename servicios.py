# ==================================================
# UNIVERSIDAD NACIONAL ABIERTA Y A DISTANCIA - UNAD
# Curso: Programación
# Fase 4 - Sistema Integral de Gestión
# Módulo: Servicios
# Autor: Johan Alexander Sanabria Cubides
# ==================================================

# Importamos herramientas para clases abstractas
from abc import ABC, abstractmethod


# =====================================================
# CLASE ABSTRACTA SERVICIO
# =====================================================

class Servicio(ABC):

    # Constructor principal
    def __init__(self, nombre):

        # Validación del nombre
        if not nombre.strip():
            raise ValueError("El nombre del servicio no puede estar vacío")

        self.nombre = nombre

    # Método abstracto para calcular costos
    @abstractmethod
    def calcular_costo(self):
        pass

    # Método abstracto para mostrar descripción
    @abstractmethod
    def descripcion(self):
        pass


# =====================================================
# CLASE RESERVA DE SALAS
# =====================================================

class ReservaSala(Servicio):

    # Constructor
    def __init__(self, nombre, valor_hora, horas):

        # Llamamos al constructor padre
        super().__init__(nombre)

        # Validaciones
        if valor_hora <= 0:
            raise ValueError("El valor por hora debe ser mayor a cero")

        if horas <= 0:
            raise ValueError("Las horas deben ser mayores a cero")

        self.valor_hora = valor_hora
        self.horas = horas

    # Método para calcular costo
    def calcular_costo(self):
        return self.valor_hora * self.horas

    # Método descripción
    def descripcion(self):
        return f"Reserva de sala por {self.horas} horas"


# =====================================================
# CLASE ALQUILER DE EQUIPOS
# =====================================================

class AlquilerEquipo(Servicio):

    # Constructor
    def __init__(self, nombre, valor_dia, dias):

        # Llamamos al constructor padre
        super().__init__(nombre)

        # Validaciones
        if valor_dia <= 0:
            raise ValueError("El valor por día debe ser mayor a cero")

        if dias <= 0:
            raise ValueError("Los días deben ser mayores a cero")

        self.valor_dia = valor_dia
        self.dias = dias

    # Método para calcular costo
    def calcular_costo(self):
        return self.valor_dia * self.dias

    # Método descripción
    def descripcion(self):
        return f"Alquiler de equipo por {self.dias} días"


# =====================================================
# CLASE ASESORIA
# =====================================================

class Asesoria(Servicio):

    # Constructor
    def __init__(self, nombre, tarifa_hora, horas):

        # Llamamos al constructor padre
        super().__init__(nombre)

        # Validaciones
        if tarifa_hora <= 0:
            raise ValueError("La tarifa por hora debe ser mayor a cero")

        if horas <= 0:
            raise ValueError("Las horas deben ser mayores a cero")

        self.tarifa_hora = tarifa_hora
        self.horas = horas

    # Método para calcular costo
    def calcular_costo(self):
        return self.tarifa_hora * self.horas

    # Método descripción
    def descripcion(self):
        return f"Asesoría especializada de {self.horas} horas"


# =====================================================
# PRUEBAS DEL MODULO
# =====================================================

try:

    # Crear servicios
    sala = ReservaSala("Sala VIP", 50000, 3)
    equipo = AlquilerEquipo("Portátil", 30000, 2)
    asesoria = Asesoria("Python", 80000, 4)

    # Mostrar información
    print("===== SERVICIOS REGISTRADOS =====")

    print("\nServicio:", sala.nombre)
    print(sala.descripcion())
    print("Costo:", sala.calcular_costo())

    print("\nServicio:", equipo.nombre)
    print(equipo.descripcion())
    print("Costo:", equipo.calcular_costo())

    print("\nServicio:", asesoria.nombre)
    print(asesoria.descripcion())
    print("Costo:", asesoria.calcular_costo())

except Exception as e:

    print("Ocurrió un error:", e)


# =====================================================
# PRUEBA DE MANEJO DE ERRORES
# =====================================================

print("\n===== PRUEBA DE ERROR =====")

try:

    # Error intencional
    error_servicio = ReservaSala("Sala Error", 50000, -2)

except Exception as e:

    print("Error detectado:", e)

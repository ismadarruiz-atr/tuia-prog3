"""
Módulo de estrategias para el juego del Tateti

Este módulo contiene las estrategias para elegir la acción a realizar.
Los alumnos deben implementar la estrategia minimax.

Por defecto, se incluye una estrategia aleatoria como ejemplo base.
"""

import random
from typing import List, Tuple
from tateti import Tateti, JUGADOR_MAX, JUGADOR_MIN

def estrategia_aleatoria(tateti: Tateti, estado: List[List[str]]) -> Tuple[int, int]:
    """
    Estrategia aleatoria: elige una acción al azar entre las disponibles.
  
    Args:
        tateti: Instancia de la clase Tateti
        estado: Estado actual del tablero
        
    Returns:
        Tuple[int, int]: Acción elegida (fila, columna)

    Raises:
        ValueError: Si no hay acciones disponibles
    """
    acciones_disponibles = tateti.acciones(estado)
    if not acciones_disponibles:
        raise ValueError("No hay acciones disponibles")
    
    return random.choice(acciones_disponibles)

def estrategia_minimax(tateti: Tateti, estado: List[List[str]]) -> Tuple[int, int]:
    """
        Estrategia minimax: elige la mejor acción usando el algoritmo minimax.
        
        Args:
            tateti: Instancia de la clase Tateti
            estado: Estado actual del tablero
            
        Returns:
            Tuple[int, int]: Acción elegida (fila, columna)
            
        Raises:
            NotImplementedError: Hasta que el alumno implemente el algoritmo
    """
    # TODO: Implementar algoritmo minimax

    # INSTRUCCIONES:
    # 1. Eliminar la línea 'raise NotImplementedError...' de abajo - DONE
    # 2. Implementar el algoritmo minimax aquí

    if tateti.jugador(estado) == JUGADOR_MAX:
        acciones_sucesoras = {accion: MINIMAX_MIN(tateti, tateti.resultado(estado, accion)) for accion in tateti.acciones(estado)}
        return max(acciones_sucesoras, key=acciones_sucesoras.get) # obtiene la clave con el mayor valor
    if tateti.jugador(estado) == JUGADOR_MIN:
        acciones_sucesoras = {accion: MINIMAX_MAX(tateti, tateti.resultado(estado, accion)) for accion in tateti.acciones(estado)}
        return min(acciones_sucesoras, key=acciones_sucesoras.get) # obtiene la clave con el menor valor


def MINIMAX_MAX(tateti: Tateti, estado :List[List[str]]) -> int:
    """Función auxiliar para el algoritmo minimax: calcula el valor máximo para MAX"""
    if tateti.test_terminal(estado):
        return tateti.utilidad(estado, JUGADOR_MAX)
    valor = -1
    for accion in tateti.acciones(estado):
        estado_sucesor = tateti.resultado(estado, accion)
        valor = max(valor, MINIMAX_MIN(tateti, estado_sucesor))
    return valor
   

def MINIMAX_MIN(tateti: Tateti, estado :List[List[str]]) -> int:
    """Función auxiliar para el algoritmo minimax: calcula el valor mínimo para MIN """
    if tateti.test_terminal(estado):
        return tateti.utilidad(estado, JUGADOR_MAX)
    valor = 2
    for accion in tateti.acciones(estado):
        estado_sucesor = tateti.resultado(estado, accion)
        valor = min(valor, MINIMAX_MAX(tateti, estado_sucesor))
    return valor

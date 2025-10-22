"""
Módulo para medir o tempo de execução dos algoritmos.
"""

import time
from functools import wraps


def measure_time(func):
    """
    Decorator para medir o tempo de execução de uma função.
    
    Args:
        func: Função a ser medida
        
    Returns:
        Wrapper que retorna (resultado, tempo_em_segundos)
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        return result, execution_time
    return wrapper


def measure_execution_time(func, *args, **kwargs):
    """
    Mede o tempo de execução de uma função.
    
    Args:
        func: Função a ser executada
        *args: Argumentos posicionais para a função
        **kwargs: Argumentos nomeados para a função
        
    Returns:
        tuple: (resultado, tempo_em_segundos)
    """
    start_time = time.perf_counter()
    result = func(*args, **kwargs)
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    
    return result, execution_time


def format_time(seconds):
    """
    Formata o tempo em uma string legível.
    
    Args:
        seconds (float): Tempo em segundos
        
    Returns:
        str: Tempo formatado
    """
    if seconds < 0.000001:  # menos de 1 microssegundo
        return f"{seconds * 1e9:.2f} ns"
    elif seconds < 0.001:  # menos de 1 milissegundo
        return f"{seconds * 1e6:.2f} µs"
    elif seconds < 1:  # menos de 1 segundo
        return f"{seconds * 1000:.2f} ms"
    else:
        return f"{seconds:.4f} s"

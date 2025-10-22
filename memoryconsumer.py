"""
Módulo para medir o consumo de memória dos algoritmos.
"""

import tracemalloc
import sys


def measure_memory(func, *args, **kwargs):
    """
    Mede o consumo de memória de uma função.
    
    Args:
        func: Função a ser executada
        *args: Argumentos posicionais para a função
        **kwargs: Argumentos nomeados para a função
        
    Returns:
        tuple: (resultado, memoria_em_bytes)
    """
    tracemalloc.start()
    
    result = func(*args, **kwargs)
    
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    return result, peak


def format_memory(bytes_value):
    """
    Formata o valor de memória em uma string legível.
    
    Args:
        bytes_value (int): Valor em bytes
        
    Returns:
        str: Memória formatada
    """
    if bytes_value < 1024:
        return f"{bytes_value} B"
    elif bytes_value < 1024 * 1024:
        return f"{bytes_value / 1024:.2f} KB"
    elif bytes_value < 1024 * 1024 * 1024:
        return f"{bytes_value / (1024 * 1024):.2f} MB"
    else:
        return f"{bytes_value / (1024 * 1024 * 1024):.2f} GB"


def get_object_size(obj):
    """
    Retorna o tamanho aproximado de um objeto em bytes.
    
    Args:
        obj: Objeto a ser medido
        
    Returns:
        int: Tamanho em bytes
    """
    return sys.getsizeof(obj)

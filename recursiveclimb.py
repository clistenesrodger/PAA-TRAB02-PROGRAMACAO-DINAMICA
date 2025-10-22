"""
Módulo para resolver o Staircase Problem usando RECURSÃO (Força Bruta).

O problema: Dado uma escada com n degraus, de quantas formas diferentes
podemos subir a escada se podemos dar passos de 1 ou 2 degraus por vez?

ABORDAGEM: Recursão pura (Força Bruta)
- Explora todas as possibilidades sem armazenar resultados intermediários
- Complexidade exponencial
"""


def climb_stairs_recursive(n):
    """
    Resolve o problema da escada usando RECURSÃO PURA (FORÇA BRUTA).
    
    Esta é a abordagem solicitada no trabalho para a versão recursiva.
    Não utiliza nenhuma otimização, explorando todas as possibilidades.
    
    Args:
        n (int): Número de degraus da escada
        
    Returns:
        int: Número de formas diferentes de subir a escada
        
    Complexidade:
        Tempo: O(2^n) - exponencial
        Espaço: O(n) - pilha de recursão
    """
    if n <= 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    
    # A solução é a soma das formas de chegar a n-1 e n-2
    return climb_stairs_recursive(n - 1) + climb_stairs_recursive(n - 2)


## Versão com memoização removida para simplificação do projeto

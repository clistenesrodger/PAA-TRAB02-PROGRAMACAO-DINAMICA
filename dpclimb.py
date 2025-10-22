"""
Módulo para resolver o Staircase Problem usando PROGRAMAÇÃO DINÂMICA.

O problema: Dado uma escada com n degraus, de quantas formas diferentes
podemos subir a escada se podemos dar passos de 1 ou 2 degraus por vez?

ABORDAGEM: Programação Dinâmica Bottom-up (Tabulação)
- Constrói a solução de baixo para cima
- Armazena resultados intermediários em uma tabela
- Complexidade linear O(n)
"""


def climb_stairs_dp(n):
    """
    Resolve o problema da escada usando PROGRAMAÇÃO DINÂMICA BOTTOM-UP.
    
    Esta é a abordagem solicitada no trabalho para a versão com PD.
    Utiliza tabulação para construir a solução de baixo para cima.
    
    Args:
        n (int): Número de degraus da escada
        
    Returns:
        int: Número de formas diferentes de subir a escada
        
    Complexidade:
        Tempo: O(n) - linear
        Espaço: O(n) - tabela dp
        
    Método: Tabulação (Bottom-up)
    - Preenche uma tabela dp[] de baixo para cima
    - dp[i] = número de formas de chegar ao degrau i
    - dp[i] = dp[i-1] + dp[i-2]
    """
    if n <= 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    
    # dp[i] representa o número de formas de chegar ao degrau i
    dp = [0] * (n + 1)
    dp[1] = 1  # 1 forma de chegar ao degrau 1
    dp[2] = 2  # 2 formas de chegar ao degrau 2 (1+1 ou 2)
    
    # Preencher a tabela de baixo para cima
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    return dp[n]


## Versão otimizada removida para simplificação do projeto

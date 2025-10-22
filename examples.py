"""
Exemplos de Uso do Staircase Problem
=====================================

Este arquivo demonstra como usar cada módulo individualmente.
"""

# Importar os módulos
from dpclimb import climb_stairs_dp
from recursiveclimb import climb_stairs_recursive
from executiontime import measure_execution_time, format_time
from memoryconsumer import measure_memory, format_memory


def exemplo_basico():
    """Exemplo básico de uso de cada implementação."""
    print("="*70)
    print("EXEMPLO 1: Uso Básico das Implementações")
    print("="*70)
    
    n = 10
    print(f"\nQuantas formas de subir uma escada com {n} degraus?\n")
    
    # Recursão Pura
    result1 = climb_stairs_recursive(n)
    print(f"Recursão Pura: {result1}")
    
    # Programação Dinâmica
    result2 = climb_stairs_dp(n)
    print(f"Programação Dinâmica: {result2}")
    
    print(f"\nAmbos retornam o mesmo resultado: {result1 == result2}")


def exemplo_comparacao_tempo():
    """Exemplo de comparação de tempo de execução."""
    print("\n" + "="*70)
    print("EXEMPLO 2: Comparação de Tempo de Execução")
    print("="*70)
    
    n = 30
    print(f"\nComparando tempo para n = {n}:\n")
    
    # Nota: Recursão pura é muito lenta para n >= 35
    if n <= 35:
        result, time_rec = measure_execution_time(climb_stairs_recursive, n)
        print(f"Recursão Pura: {format_time(time_rec)}")
    
    result, time_dp = measure_execution_time(climb_stairs_dp, n)
    print(f"Programação Dinâmica: {format_time(time_dp)}")


def exemplo_comparacao_memoria():
    """Exemplo de comparação de uso de memória."""
    print("\n" + "="*70)
    print("EXEMPLO 3: Comparação de Uso de Memória")
    print("="*70)
    
    n = 100
    print(f"\nComparando memória para n = {n}:\n")
    
    result, mem_dp = measure_memory(climb_stairs_dp, n)
    print(f"Programação Dinâmica: {format_memory(mem_dp)}")
    
    print(f"\nComparação simplificada: apenas Recursão Pura vs DP Bottom-up")


def exemplo_valores_crescentes():
    """Exemplo mostrando valores crescentes."""
    print("\n" + "="*70)
    print("EXEMPLO 4: Valores para Diferentes Tamanhos de Escada")
    print("="*70)
    
    print("\n{:>5} | {:>20}".format("N", "Número de Formas"))
    print("-" * 30)
    
    for n in range(1, 21):
        result = climb_stairs_dp(n)
        print(f"{n:5} | {result:20}")


def exemplo_relacao_fibonacci():
    """Mostra a relação com a sequência de Fibonacci."""
    print("\n" + "="*70)
    print("EXEMPLO 5: Relação com Fibonacci")
    print("="*70)
    
    print("\nO Staircase Problem segue a sequência de Fibonacci!")
    print("\n{:>5} | {:>15} | {:>15}".format("N", "Staircase", "Fibonacci"))
    print("-" * 40)
    
    # Fibonacci tradicional
    def fibonacci(n):
        if n <= 1:
            return n
        a, b = 0, 1
        for _ in range(2, n + 2):
            a, b = b, a + b
        return b
    
    for n in range(1, 15):
        stairs = climb_stairs_dp(n)
        fib = fibonacci(n)
        print(f"{n:5} | {stairs:15} | {fib:15}")
    
    print("\nObserve que staircase(n) = fibonacci(n+1)!")


def exemplo_grande():
    """Exemplo com valores grandes."""
    print("\n" + "="*70)
    print("EXEMPLO 6: Lidando com Valores Grandes")
    print("="*70)
    
    print("\nA PD pode lidar com valores muito grandes rapidamente:\n")
    
    for n in [100, 500, 1000]:
        result, time = measure_execution_time(climb_stairs_dp, n)
        print(f"n = {n:4}: {result} (tempo: {format_time(time)})")
    
    print("\nNota: A recursão pura seria inviável para esses valores!")


if __name__ == "__main__":
    exemplo_basico()
    exemplo_comparacao_tempo()
    exemplo_comparacao_memoria()
    exemplo_valores_crescentes()
    exemplo_relacao_fibonacci()
    exemplo_grande()
    
    print("\n" + "="*70)
    print("Todos os exemplos foram executados com sucesso!")
    print("="*70 + "\n")

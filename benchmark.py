"""
Módulo de Benchmark - Staircase Problem

Realiza benchmark das implementações com:
- Conjunto fixo de dados (inputs.txt)
- 30 execuções para cada tamanho
- Cálculo da mediana do tempo e memória
"""

import statistics
import time
import tracemalloc
from dpclimb import climb_stairs_dp
from recursiveclimb import climb_stairs_recursive
from executiontime import format_time
from memoryconsumer import format_memory


def read_inputs(filename='inputs.txt'):
    """
    Lê o arquivo de inputs com os tamanhos das escadas.
    
    Args:
        filename (str): Nome do arquivo de inputs
        
    Returns:
        list: Lista de valores inteiros (tamanhos das escadas)
    """
    inputs = []
    try:
        with open(filename, 'r') as f:
            for line in f:
                line = line.strip()
                # Ignora linhas vazias e comentários
                if line and not line.startswith('#'):
                    try:
                        value = int(line)
                        if value > 0:
                            inputs.append(value)
                    except ValueError:
                        print(f"Aviso: Ignorando linha inválida: {line}")
    except FileNotFoundError:
        print(f"Erro: Arquivo '{filename}' não encontrado.")
        print("Usando valores padrão: 100, 1000, 10000")
        inputs = [100, 1000, 10000]
    
    return inputs


def measure_single_execution(func, n):
    """
    Mede tempo e memória de uma única execução.
    
    Args:
        func: Função a ser executada
        n (int): Parâmetro para a função
        
    Returns:
        tuple: (tempo_em_segundos, memoria_em_bytes)
    """
    # Medir memória
    tracemalloc.start()
    
    # Medir tempo
    start_time = time.perf_counter()
    result = func(n)
    end_time = time.perf_counter()
    
    # Obter memória
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    execution_time = end_time - start_time
    memory_used = peak
    
    return execution_time, memory_used


def run_benchmark(func, n, num_executions=30):
    """
    Executa benchmark com múltiplas execuções.
    
    Args:
        func: Função a ser testada
        n (int): Tamanho da entrada
        num_executions (int): Número de execuções (padrão: 30)
        
    Returns:
        dict: Dicionário com estatísticas
    """
    times = []
    memories = []
    
    print(f"  Executando {num_executions} vezes...", end='', flush=True)
    
    for i in range(num_executions):
        exec_time, memory = measure_single_execution(func, n)
        times.append(exec_time)
        memories.append(memory)
        
        # Indicador de progresso
        if (i + 1) % 10 == 0:
            print(f" {i+1}", end='', flush=True)
    
    print(" ✓")
    
    # Calcular estatísticas
    stats = {
        'median_time': statistics.median(times),
        'mean_time': statistics.mean(times),
        'min_time': min(times),
        'max_time': max(times),
        'stdev_time': statistics.stdev(times) if len(times) > 1 else 0,
        'median_memory': statistics.median(memories),
        'mean_memory': statistics.mean(memories),
        'min_memory': min(memories),
        'max_memory': max(memories),
        'stdev_memory': statistics.stdev(memories) if len(memories) > 1 else 0,
        'num_executions': num_executions
    }
    
    return stats


def print_benchmark_header():
    """Imprime o cabeçalho do benchmark."""
    print("\n" + "="*80)
    print(" "*20 + "BENCHMARK - STAIRCASE PROBLEM")
    print("="*80)
    print("\nConfiguração:")
    print("  • Número de execuções por teste: 30")
    print("  • Métrica principal: MEDIANA")
    print("  • Conjunto de dados: inputs.txt")
    print("="*80 + "\n")


def print_results_table(results):
    """
    Imprime tabela com os resultados do benchmark.
    
    Args:
        results (dict): Dicionário com resultados organizados
    """
    from tabulate import tabulate
    
    print("\n" + "="*80)
    print("RESULTADOS DO BENCHMARK (MEDIANA)")
    print("="*80 + "\n")
    
    for algo_name, algo_results in results.items():
        print(f"\n{algo_name}")
        print("-" * 80)
        
        table_data = []
        for n, stats in algo_results.items():
            row = [
                n,
                format_time(stats['median_time']),
                format_memory(int(stats['median_memory'])),
                format_time(stats['mean_time']),
                format_time(stats['stdev_time']),
                stats['num_executions']
            ]
            table_data.append(row)
        
        headers = ['N', 'Tempo (Mediana)', 'Memória (Mediana)', 
                   'Tempo (Média)', 'Desvio Padrão', 'Execuções']
        print(tabulate(table_data, headers=headers, tablefmt='grid'))


def save_results_to_file(results, filename='benchmark_results.txt'):
    """
    Salva os resultados detalhados em arquivo texto.
    
    Args:
        results (dict): Resultados do benchmark
        filename (str): Nome do arquivo de saída
    """
    with open(filename, 'w', encoding='utf-8') as f:
        f.write("="*80 + "\n")
        f.write("RESULTADOS DO BENCHMARK - STAIRCASE PROBLEM\n")
        f.write("="*80 + "\n\n")
        f.write("Configuração:\n")
        f.write("  • Número de execuções por teste: 30\n")
        f.write("  • Métrica principal: MEDIANA\n")
        f.write("  • Conjunto de dados: inputs.txt (100, 1000, 10000)\n")
        f.write("\n" + "="*80 + "\n\n")
        
        for algo_name, algo_results in results.items():
            f.write(f"\n{'='*80}\n")
            f.write(f"{algo_name}\n")
            f.write(f"{'='*80}\n\n")
            
            for n, stats in algo_results.items():
                f.write(f"Tamanho da Escada (N): {n}\n")
                f.write(f"{'-'*40}\n")
                f.write(f"Tempo de Execução:\n")
                f.write(f"  • Mediana: {format_time(stats['median_time'])}\n")
                f.write(f"  • Média:   {format_time(stats['mean_time'])}\n")
                f.write(f"  • Mínimo:  {format_time(stats['min_time'])}\n")
                f.write(f"  • Máximo:  {format_time(stats['max_time'])}\n")
                f.write(f"  • Desvio:  {format_time(stats['stdev_time'])}\n")
                f.write(f"\nConsumo de Memória:\n")
                f.write(f"  • Mediana: {format_memory(int(stats['median_memory']))}\n")
                f.write(f"  • Média:   {format_memory(int(stats['mean_memory']))}\n")
                f.write(f"  • Mínimo:  {format_memory(int(stats['min_memory']))}\n")
                f.write(f"  • Máximo:  {format_memory(int(stats['max_memory']))}\n")
                f.write(f"  • Desvio:  {format_memory(int(stats['stdev_memory']))}\n")
                f.write(f"\nNúmero de Execuções: {stats['num_executions']}\n")
                f.write(f"\n")
    
    print(f"\n✓ Resultados detalhados salvos em: {filename}")


def save_results_to_csv(results, filename='benchmark_results.csv'):
    """
    Salva os resultados em formato CSV.
    
    Args:
        results (dict): Resultados do benchmark
        filename (str): Nome do arquivo CSV
    """
    import csv
    
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = [
            'Algoritmo', 'N', 
            'Mediana_Tempo_s', 'Media_Tempo_s', 'Min_Tempo_s', 'Max_Tempo_s', 'DP_Tempo_s',
            'Mediana_Memoria_bytes', 'Media_Memoria_bytes', 'Min_Memoria_bytes', 
            'Max_Memoria_bytes', 'DP_Memoria_bytes',
            'Num_Execucoes'
        ]
        
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        
        for algo_name, algo_results in results.items():
            for n, stats in algo_results.items():
                row = {
                    'Algoritmo': algo_name,
                    'N': n,
                    'Mediana_Tempo_s': stats['median_time'],
                    'Media_Tempo_s': stats['mean_time'],
                    'Min_Tempo_s': stats['min_time'],
                    'Max_Tempo_s': stats['max_time'],
                    'DP_Tempo_s': stats['stdev_time'],
                    'Mediana_Memoria_bytes': int(stats['median_memory']),
                    'Media_Memoria_bytes': int(stats['mean_memory']),
                    'Min_Memoria_bytes': int(stats['min_memory']),
                    'Max_Memoria_bytes': int(stats['max_memory']),
                    'DP_Memoria_bytes': int(stats['stdev_memory']),
                    'Num_Execucoes': stats['num_executions']
                }
                writer.writerow(row)
    
    print(f"✓ Resultados salvos em CSV: {filename}")


def run_full_benchmark(input_file='inputs.txt', num_executions=30):
    """
    Executa o benchmark completo.
    
    Args:
        input_file (str): Arquivo com os tamanhos das escadas
        num_executions (int): Número de execuções por teste
    """
    print_benchmark_header()
    
    # Ler inputs
    inputs = read_inputs(input_file)
    print(f"Tamanhos das escadas (inputs.txt): {inputs}\n")
    
    # Definir algoritmos a serem testados
    algorithms = {
        '1. Recursão Pura (FORÇA BRUTA)': (climb_stairs_recursive, None),
        '2. Programação Dinâmica BOTTOM-UP': (climb_stairs_dp, None),
    }
    
    results = {}
    
    # Executar benchmark para cada algoritmo
    for algo_name, (func, max_n) in algorithms.items():
        print(f"\n{'='*80}")
        print(f"Testando: {algo_name}")
        print(f"{'='*80}")
        
        results[algo_name] = {}
        
        for n in inputs:
            # Verificar se n excede o limite para o algoritmo
            if max_n is not None and n > max_n:
                print(f"\nN = {n}: PULADO (muito lento para este algoritmo)")
                continue
            
            print(f"\nN = {n}:")
            try:
                stats = run_benchmark(func, n, num_executions)
                results[algo_name][n] = stats
                
                # Mostrar resultado imediato
                print(f"  → Mediana Tempo: {format_time(stats['median_time'])}")
                print(f"  → Mediana Memória: {format_memory(int(stats['median_memory']))}")
                
            except Exception as e:
                print(f"  ✗ Erro: {str(e)}")
    
    # Imprimir resultados
    print_results_table(results)
    
    # Salvar resultados
    save_results_to_file(results)
    save_results_to_csv(results)
    
    return results


def main():
    """Função principal."""
    import sys
    
    # Verificar argumentos
    num_executions = 30
    if len(sys.argv) > 1:
        try:
            num_executions = int(sys.argv[1])
        except ValueError:
            print(f"Aviso: Argumento inválido '{sys.argv[1]}', usando padrão (30)")
    
    # Executar benchmark
    results = run_full_benchmark(num_executions=num_executions)
    
    print("\n" + "="*80)
    print("BENCHMARK CONCLUÍDO!")
    print("="*80)
    print("\nArquivos gerados:")
    print("  • benchmark_results.txt - Resultados detalhados")
    print("  • benchmark_results.csv - Dados em formato CSV")
    print("\n")


if __name__ == "__main__":
    main()

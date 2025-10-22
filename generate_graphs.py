#!/usr/bin/env python3
"""
Gerador de Gráficos - Análise de Benchmark

Gera gráficos a partir do arquivo benchmark_results.csv:
1. Gráfico de barras - Comparação de tempo de execução
2. Gráfico de linhas - Comparação de consumo de memória

Uso:
    python generate_graphs.py
    python generate_graphs.py benchmark_results.csv
"""

import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path


def format_time_axis(seconds):
    """Formata tempo para o eixo Y do gráfico."""
    if seconds < 1e-6:
        return f'{seconds*1e9:.1f} ns'
    elif seconds < 1e-3:
        return f'{seconds*1e6:.1f} µs'
    elif seconds < 1:
        return f'{seconds*1e3:.1f} ms'
    else:
        return f'{seconds:.2f} s'


def format_memory_axis(bytes_val):
    """Formata memória para o eixo Y do gráfico."""
    if bytes_val < 1024:
        return f'{bytes_val:.0f} B'
    elif bytes_val < 1024**2:
        return f'{bytes_val/1024:.1f} KB'
    elif bytes_val < 1024**3:
        return f'{bytes_val/1024**2:.1f} MB'
    else:
        return f'{bytes_val/1024**3:.1f} GB'


def generate_time_bar_chart(df, output_file='grafico_tempo.png'):
    """
    Gera gráfico de barras comparando tempo de execução.
    
    Args:
        df: DataFrame com os dados do benchmark
        output_file: Nome do arquivo de saída
    """
    # Preparar dados
    algorithms = df['Algoritmo'].unique()
    n_values = sorted(df['N'].unique())
    
    # Configurar figura
    fig, ax = plt.subplots(figsize=(12, 7))
    
    # Largura das barras
    x = np.arange(len(n_values))
    width = 0.35
    
    # Cores
    colors = ['#e74c3c', '#3498db']  # Vermelho para Brute, Azul para DP
    
    # Plotar barras para cada algoritmo
    for i, algo in enumerate(algorithms):
        algo_data = df[df['Algoritmo'] == algo].sort_values('N')
        times = algo_data['Mediana_Tempo_s'].values
        
        bars = ax.bar(x + i*width, times, width, label=algo.split('. ')[1], 
                      color=colors[i], alpha=0.8, edgecolor='black', linewidth=0.5)
        
        # Adicionar rótulos nas barras
        for j, (bar, time) in enumerate(zip(bars, times)):
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height,
                   format_time_axis(time),
                   ha='center', va='bottom', fontsize=8, rotation=0)
    
    # Configurar eixos e labels
    ax.set_xlabel('Tamanho da Escada (N)', fontsize=12, fontweight='bold')
    ax.set_ylabel('Tempo de Execução (escala logarítmica)', fontsize=12, fontweight='bold')
    ax.set_title('Comparação de Tempo de Execução - Força Bruta vs Programação Dinâmica',
                 fontsize=14, fontweight='bold', pad=20)
    ax.set_xticks(x + width / 2)
    ax.set_xticklabels(n_values)
    ax.legend(loc='upper left', fontsize=10)
    ax.grid(True, alpha=0.3, axis='y', linestyle='--')
    
    # Escala logarítmica no eixo Y (tempo cresce exponencialmente)
    ax.set_yscale('log')
    
    # Ajustar layout
    plt.tight_layout()
    
    # Salvar
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    print(f'✓ Gráfico de tempo salvo: {output_file}')
    
    return fig


def generate_memory_line_chart(df, output_file='grafico_memoria.png'):
    """
    Gera gráfico de linha comparando consumo de memória.
    
    Args:
        df: DataFrame com os dados do benchmark
        output_file: Nome do arquivo de saída
    """
    # Preparar dados
    algorithms = df['Algoritmo'].unique()
    
    # Configurar figura
    fig, ax = plt.subplots(figsize=(12, 7))
    
    # Cores e estilos
    colors = ['#e74c3c', '#3498db']  # Vermelho para Brute, Azul para DP
    markers = ['o', 's']  # Círculo e quadrado
    linestyles = ['-', '--']
    
    # Plotar linhas para cada algoritmo
    for i, algo in enumerate(algorithms):
        algo_data = df[df['Algoritmo'] == algo].sort_values('N')
        n_values = algo_data['N'].values
        memory = algo_data['Mediana_Memoria_bytes'].values
        
        # Plotar linha
        ax.plot(n_values, memory, marker=markers[i], linestyle=linestyles[i],
               color=colors[i], linewidth=2.5, markersize=8, alpha=0.8,
               label=algo.split('. ')[1], markeredgecolor='black', markeredgewidth=0.5)
        
        # Adicionar rótulos nos pontos
        for n, mem in zip(n_values, memory):
            ax.annotate(format_memory_axis(mem),
                       (n, mem),
                       textcoords="offset points",
                       xytext=(0, 10),
                       ha='center',
                       fontsize=8,
                       bbox=dict(boxstyle='round,pad=0.3', facecolor=colors[i], alpha=0.3))
    
    # Configurar eixos e labels
    ax.set_xlabel('Tamanho da Escada (N)', fontsize=12, fontweight='bold')
    ax.set_ylabel('Consumo de Memória (bytes)', fontsize=12, fontweight='bold')
    ax.set_title('Comparação de Consumo de Memória - Força Bruta vs Programação Dinâmica',
                 fontsize=14, fontweight='bold', pad=20)
    ax.legend(loc='upper left', fontsize=10)
    ax.grid(True, alpha=0.3, linestyle='--')
    
    # Ajustar layout
    plt.tight_layout()
    
    # Salvar
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    print(f'✓ Gráfico de memória salvo: {output_file}')
    
    return fig


def main():
    """Função principal."""
    # Verificar argumentos
    csv_file = sys.argv[1] if len(sys.argv) > 1 else 'benchmark_results.csv'
    
    # Verificar se arquivo existe
    if not Path(csv_file).exists():
        print(f'Erro: Arquivo {csv_file} não encontrado.')
        print('Execute o benchmark primeiro: python benchmark.py')
        sys.exit(1)
    
    print('='*80)
    print(' '*20 + 'GERADOR DE GRÁFICOS - BENCHMARK')
    print('='*80)
    print(f'\nLendo dados de: {csv_file}')
    
    # Ler CSV
    try:
        df = pd.read_csv(csv_file)
        print(f'✓ {len(df)} registros carregados')
        print(f'  - Algoritmos: {", ".join(df["Algoritmo"].unique())}')
        print(f'  - Valores de N: {sorted(df["N"].unique())}')
    except Exception as e:
        print(f'Erro ao ler CSV: {e}')
        sys.exit(1)
    
    print('\n' + '-'*80)
    print('Gerando gráficos...')
    print('-'*80 + '\n')
    
    # Gerar gráficos
    try:
        # 1. Gráfico de tempo (barras)
        generate_time_bar_chart(df, 'grafico_tempo.png')
        
        # 2. Gráfico de memória (linhas)
        generate_memory_line_chart(df, 'grafico_memoria.png')
        
        print('\n' + '='*80)
        print('✓ TODOS OS GRÁFICOS FORAM GERADOS COM SUCESSO!')
        print('='*80)
        print('\nArquivos gerados:')
        print('  • grafico_tempo.png - Comparação de tempo de execução (barras)')
        print('  • grafico_memoria.png - Comparação de consumo de memória (linhas)')
        print('\n')
        
    except Exception as e:
        print(f'\nErro ao gerar gráficos: {e}')
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()

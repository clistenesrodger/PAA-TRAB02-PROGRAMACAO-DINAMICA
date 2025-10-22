"""
Programa Principal - Staircase Problem

Este programa compara diferentes implementações para resolver o problema da escada.

IMPLEMENTAÇÕES PRINCIPAIS (Solicitadas no Trabalho):
1. Recursão Pura (Força Bruta) - Abordagem Recursiva
2. Programação Dinâmica Bottom-up - Abordagem com PD

Observação: versões auxiliares foram removidas para simplificação do projeto
"""

import sys
from dpclimb import climb_stairs_dp
from recursiveclimb import climb_stairs_recursive
from executiontime import measure_execution_time, format_time
from memoryconsumer import measure_memory, format_memory
from datasheet import DataSheet


def print_header():
    """Imprime o cabeçalho do programa."""
    print("\n" + "="*80)
    print(" "*20 + "STAIRCASE PROBLEM - ANÁLISE COMPARATIVA")
    print("="*80)
    print("\nProblema: Dado uma escada com N degraus, de quantas formas diferentes")
    print("podemos subir a escada se podemos dar passos de 1 ou 2 degraus por vez?")
    print("\n" + "="*80)
    print("IMPLEMENTAÇÕES PRINCIPAIS (Solicitadas):")
    print("="*80)
    print("  1. Recursão Pura (FORÇA BRUTA) - Abordagem Recursiva")
    print("  2. Programação Dinâmica BOTTOM-UP - Abordagem com PD")
    print("\n" + "-"*80)
    print("Projeto simplificado: apenas Força Bruta e DP Bottom-up")
    print("="*80 + "\n")


def test_algorithm(name, func, n, datasheet):
    """
    Testa um algoritmo e registra os resultados.
    
    Args:
        name (str): Nome do algoritmo
        func: Função a ser testada
        n (int): Número de degraus
        datasheet (DataSheet): Objeto para armazenar resultados
    """
    print(f"\nTestando: {name} com n={n}")
    print("-" * 60)
    
    try:
        # Medir tempo e memória
        result, memory = measure_memory(func, n)
        _, exec_time = measure_execution_time(func, n)
        
        print(f"Resultado: {result}")
        print(f"Tempo de execução: {format_time(exec_time)}")
        print(f"Consumo de memória: {format_memory(memory)}")
        
        # Adicionar ao datasheet
        datasheet.add_record(name, n, result, exec_time, memory)
        
        return True
    except RecursionError:
        print(f"ERRO: Limite de recursão excedido para n={n}")
        return False
    except Exception as e:
        print(f"ERRO: {str(e)}")
        return False


def run_comparison(test_values, skip_recursive=False):
    """
    Executa comparação entre os algoritmos.
    
    Args:
        test_values (list): Lista de valores de n para testar
        skip_recursive (bool): Se True, pula recursão pura para valores grandes
    """
    datasheet = DataSheet()
    
    for n in test_values:
        print(f"\n{'='*80}")
        print(f"TESTANDO COM N = {n}")
        print(f"{'='*80}")
        
        print("\n" + ">>> IMPLEMENTAÇÕES PRINCIPAIS <<<".center(60))
        print("-"*60)
        
        # 1. RECURSÃO PURA (FORÇA BRUTA) - Abordagem Recursiva
        if not skip_recursive:
            test_algorithm("1. Recursão Pura (FORÇA BRUTA)", climb_stairs_recursive, n, datasheet)
        else:
            print(f"\n1. Recursão Pura (FORÇA BRUTA): Pulada (skip_recursive=True)")
        
        # 2. PROGRAMAÇÃO DINÂMICA BOTTOM-UP
        test_algorithm("2. Programação Dinâmica BOTTOM-UP", climb_stairs_dp, n, datasheet)
        
    # Implementações auxiliares removidas
    
    # Exibir resultados
    datasheet.display()
    datasheet.display_summary()
    
    # Salvar em CSV
    save = input("\nDeseja salvar os resultados em CSV? (s/n): ").strip().lower()
    if save == 's':
        filename = input("Nome do arquivo (Enter para nome padrão): ").strip()
        if filename:
            if not filename.endswith('.csv'):
                filename += '.csv'
            datasheet.save_to_csv(filename)
        else:
            datasheet.save_to_csv()


def interactive_mode():
    """Modo interativo para testar valores específicos."""
    print_header()
    
    print("MODO INTERATIVO")
    print("-" * 80)
    print("Digite os valores de N para testar (separados por vírgula)")
    print("Exemplo: 5,10,15,20,25")
    print("Ou digite 'demo' para usar valores de demonstração")
    
    user_input = input("\nValores de N: ").strip()
    
    if user_input.lower() == 'demo':
        test_values = [5, 10, 15, 20, 25, 30]
        print(f"\nUsando valores de demonstração: {test_values}")
    else:
        try:
            test_values = [int(x.strip()) for x in user_input.split(',')]
            test_values.sort()
        except ValueError:
            print("ERRO: Entrada inválida. Usando valores padrão.")
            test_values = [5, 10, 15, 20]
    
    # Verificar se há valores grandes
    max_value = max(test_values)
    skip_recursive = False
    
    if max_value > 35:
        print(f"\nAVISO: Valor máximo = {max_value}")
        print("A recursão pura será muito lenta para valores > 35")
        skip = input("Deseja pular a recursão pura? (s/n): ").strip().lower()
        skip_recursive = (skip == 's')
    
    run_comparison(test_values, skip_recursive)


def main():
    """Função principal."""
    print_header()
    
    if len(sys.argv) > 1:
        # Modo linha de comando
        try:
            test_values = [int(x) for x in sys.argv[1:]]
            test_values.sort()
            print(f"Testando com valores: {test_values}\n")
            run_comparison(test_values)
        except ValueError:
            print("ERRO: Argumentos inválidos. Use números inteiros.")
            print("Exemplo: python main.py 5 10 15 20")
            sys.exit(1)
    else:
        # Modo interativo
        interactive_mode()
    
    print("\n" + "="*80)
    print(" "*25 + "ANÁLISE CONCLUÍDA")
    print("="*80 + "\n")


if __name__ == "__main__":
    main()

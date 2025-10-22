#!/usr/bin/env python3
"""
Mede o tempo REAL (wall-clock) de uma única execução de um algoritmo
para o problema da escada. Útil para comparar FORÇA BRUTA vs DP Bottom-up
sem estatísticas (mediana/média) – apenas o tempo direto de uma rodada.

Uso:
    python measure_realtime.py --algo brute -n 30
    python measure_realtime.py --algo dp -n 900
    python measure_realtime.py --algo dp --from-inputs   # usa inputs.txt

Opções:
  --repeat R            Executa R vezes e mostra o tempo de cada uma e média simples
  --from-inputs         Lê N do arquivo inputs.txt (uma execução por N)
  --no-digits           Não calcula/mostra número de dígitos do resultado

Observações:
    - Força Bruta tem limite de segurança N <= 35 (evita travar a máquina)
"""

import argparse
import time
from typing import Callable, List

from dpclimb import climb_stairs_dp
from recursiveclimb import climb_stairs_recursive

DEFAULT_INPUTS_FILE = 'inputs.txt'


def read_inputs(file_path: str = DEFAULT_INPUTS_FILE) -> List[int]:
    values = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith('#'):
                    continue
                try:
                    values.append(int(line))
                except ValueError:
                    pass
    except FileNotFoundError:
        print(f"Aviso: arquivo {file_path} não encontrado.")
    return values


def human_time(seconds: float) -> str:
    if seconds < 1e-6:
        return f"{seconds*1e9:.2f} ns"
    if seconds < 1e-3:
        return f"{seconds*1e6:.2f} µs"
    if seconds < 1:
        return f"{seconds*1e3:.2f} ms"
    if seconds < 60:
        return f"{seconds:.2f} s"
    if seconds < 3600:
        return f"{seconds/60:.2f} min"
    return f"{seconds/3600:.2f} h"


def measure_once(func: Callable[[int], int], n: int, show_digits: bool = True) -> float:
    start = time.perf_counter()
    result = func(n)
    end = time.perf_counter()
    elapsed = end - start
    if show_digits:
        # Evitar custo de conversão muito grande quando n é pequeno está ok; para n grandes, custo é aceitável fora da medição
        try:
            digits = len(str(result))
            print(f"  • Resultado tem {digits} dígitos")
        except Exception:
            pass
    return elapsed


def main():
    parser = argparse.ArgumentParser(description='Medir tempo real (uma rodada) de um algoritmo (brute, dp).')
    parser.add_argument('--algo', choices=['brute', 'dp'], required=True, help='Algoritmo: brute (força bruta), dp (bottom-up com tabela)')
    parser.add_argument('-n', type=int, help='Tamanho N da escada')
    parser.add_argument('--from-inputs', action='store_true', help='Ler Ns de inputs.txt e medir uma vez cada')
    parser.add_argument('--repeat', type=int, default=1, help='Repetições por medição (default: 1)')
    parser.add_argument('--no-digits', action='store_true', help='Não calcular/mostrar número de dígitos do resultado')
    args = parser.parse_args()

    # Selecionar função
    if args.algo == 'brute':
        func = climb_stairs_recursive
        algo_name = 'Recursão Pura (FORÇA BRUTA)'
        max_n = None
    elif args.algo == 'dp':
        func = climb_stairs_dp
        algo_name = 'Programação Dinâmica BOTTOM-UP'
        max_n = None

    # Determinar lista de Ns
    ns: List[int] = []
    if args.from_inputs:
        ns = read_inputs(DEFAULT_INPUTS_FILE)
        if not ns:
            print('Nenhum valor encontrado em inputs.txt')
            return
    elif args.n is not None:
        ns = [args.n]
    else:
        print('Informe -n N ou use --from-inputs')
        return

    print('\n' + '='*80)
    print(f'MEDIDA DE TEMPO REAL - {algo_name}')
    print('='*80 + '\n')

    for n in ns:
        print(f'N = {n}:')
        times = []
        for i in range(args.repeat):
            t = measure_once(func, n, show_digits=not args.no_digits)
            times.append(t)
            print(f'  Execução {i+1}: {human_time(t)}')
        if len(times) > 1:
            avg = sum(times) / len(times)
            print(f'  Média simples: {human_time(avg)}')
        print()


if __name__ == '__main__':
    main()

"""
Módulo para coletar, armazenar e exibir dados de desempenho dos algoritmos.
"""

import csv
from datetime import datetime
from tabulate import tabulate


class DataSheet:
    """Classe para gerenciar dados de desempenho dos algoritmos."""
    
    def __init__(self):
        """Inicializa a planilha de dados."""
        self.data = []
        self.headers = ['Algoritmo', 'N', 'Resultado', 'Tempo (s)', 'Memória (bytes)']
    
    def add_record(self, algorithm, n, result, execution_time, memory_usage):
        """
        Adiciona um registro de execução.
        
        Args:
            algorithm (str): Nome do algoritmo
            n (int): Tamanho da entrada
            result (int): Resultado obtido
            execution_time (float): Tempo de execução em segundos
            memory_usage (int): Uso de memória em bytes
        """
        record = {
            'algorithm': algorithm,
            'n': n,
            'result': result,
            'execution_time': execution_time,
            'memory_usage': memory_usage
        }
        self.data.append(record)
    
    def display(self):
        """Exibe os dados em formato de tabela."""
        if not self.data:
            print("Nenhum dado disponível.")
            return
        
        table_data = []
        for record in self.data:
            row = [
                record['algorithm'],
                record['n'],
                record['result'],
                f"{record['execution_time']:.6f}",
                record['memory_usage']
            ]
            table_data.append(row)
        
        print("\n" + "="*80)
        print("RESULTADOS DA ANÁLISE DE DESEMPENHO")
        print("="*80)
        print(tabulate(table_data, headers=self.headers, tablefmt='grid'))
        print("="*80 + "\n")
    
    def save_to_csv(self, filename=None):
        """
        Salva os dados em um arquivo CSV.
        
        Args:
            filename (str): Nome do arquivo (opcional)
        """
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"staircase_results_{timestamp}.csv"
        
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['algorithm', 'n', 'result', 'execution_time', 'memory_usage']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            for record in self.data:
                writer.writerow(record)
        
        print(f"Dados salvos em: {filename}")
    
    def get_summary(self):
        """
        Retorna um resumo estatístico dos dados.
        
        Returns:
            dict: Resumo com estatísticas por algoritmo
        """
        if not self.data:
            return {}
        
        summary = {}
        
        for record in self.data:
            algo = record['algorithm']
            if algo not in summary:
                summary[algo] = {
                    'count': 0,
                    'total_time': 0,
                    'total_memory': 0,
                    'avg_time': 0,
                    'avg_memory': 0
                }
            
            summary[algo]['count'] += 1
            summary[algo]['total_time'] += record['execution_time']
            summary[algo]['total_memory'] += record['memory_usage']
        
        # Calcular médias
        for algo in summary:
            count = summary[algo]['count']
            summary[algo]['avg_time'] = summary[algo]['total_time'] / count
            summary[algo]['avg_memory'] = summary[algo]['total_memory'] / count
        
        return summary
    
    def display_summary(self):
        """Exibe um resumo estatístico dos dados."""
        summary = self.get_summary()
        
        if not summary:
            print("Nenhum dado disponível para resumo.")
            return
        
        print("\n" + "="*80)
        print("RESUMO ESTATÍSTICO")
        print("="*80)
        
        summary_data = []
        for algo, stats in summary.items():
            row = [
                algo,
                stats['count'],
                f"{stats['avg_time']:.6f}",
                f"{stats['avg_memory']:.2f}"
            ]
            summary_data.append(row)
        
        headers = ['Algoritmo', 'Execuções', 'Tempo Médio (s)', 'Memória Média (bytes)']
        print(tabulate(summary_data, headers=headers, tablefmt='grid'))
        print("="*80 + "\n")

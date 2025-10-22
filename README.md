# PAA-TRAB02-PROGRAMACAO-DINAMICA

## Staircase Problem - Análise Comparativa

Este projeto implementa e compara diferentes abordagens para resolver o **Staircase Problem** (Problema da Escada):

**Problema:** Dado uma escada com N degraus, de quantas formas diferentes podemos subir a escada se podemos dar passos de 1 ou 2 degraus por vez?

## 📁 Estrutura do Projeto

```
PAA-TRAB02-PROGRAMACAO-DINAMICA/
│
├── README.md            # Este arquivo - visão geral do projeto
├── ABORDAGENS.md        # Detalhamento das 2 abordagens principais
├── requirements.txt     # Dependências do projeto
├── run.sh               # Script para executar facilmente
│
├── inputs.txt           # 📊 Conjunto de dados para benchmark
│
├── dpclimb.py           # 🎯 Programação Dinâmica (Bottom-up)
├── recursiveclimb.py    # 🔄 Recursão Pura (Força Bruta)
├── executiontime.py     # ⏱️  Medição de tempo de execução
├── memoryconsumer.py    # 💾 Medição de consumo de memória
├── datasheet.py         # 📊 Coleta e exibição de dados
│
├── main.py              # 🚀 Programa principal (análise comparativa)
├── benchmark.py         # 📊 Benchmark (execuções múltiplas, mediana)
├── measure_realtime.py  # ⏱️ Medida de tempo real (uma rodada)
├── examples.py          # 📚 Exemplos de uso
└── test_staircase.py    # ✅ Testes unitários
```

## 🎯 Implementações Principais

Projeto simplificado: mantidas apenas as duas abordagens solicitadas.

### 1. **ABORDAGEM RECURSIVA (Força Bruta)**
   - Arquivo: `recursiveclimb.py`
   - Função: `climb_stairs_recursive(n)`
   - Método: Recursão pura sem otimização
   - Complexidade de Tempo: O(2^n)
   - Complexidade de Espaço: O(n) - pilha de recursão

### 2. **PROGRAMAÇÃO DINÂMICA (Bottom-up)**
   - Arquivo: `dpclimb.py`
   - Função: `climb_stairs_dp(n)`
   - Método: Tabulação de baixo para cima
   - Complexidade de Tempo: O(n)
   - Complexidade de Espaço: O(n)

## 🔧 Implementações Auxiliares

Observação: versões auxiliares (Memoização e DP Otimizada) foram removidas para simplificar o projeto.

## 🚀 Como Executar

### Pré-requisitos

Certifique-se de ter Python 3.6+ instalado.

### Instalação

```bash
# Clone o repositório (se ainda não estiver clonado)
git clone <url-do-repositorio>
cd PAA-TRAB02-PROGRAMACAO-DINAMICA

# Instale as dependências
pip install -r requirements.txt
```

### Execução

**Análise Comparativa (Modo Interativo):**
```bash
python main.py
```

**Análise Comparativa (Linha de Comando):**
```bash
# Testar com valores específicos
python main.py 5 10 15 20 25

# Exemplo com valores maiores
python main.py 10 20 30 40 50
```

**Benchmark Completo (30 execuções, mediana):**
```bash
# Usa conjunto de dados do inputs.txt (100, 1000, 10000)
python benchmark.py

# Personalizar número de execuções (ex: 50)
python benchmark.py 50
```

**Executar Testes Unitários:**
```bash
python test_staircase.py
```

**Ver Exemplos de Uso:**
```bash
python examples.py
```

## 📊 Exemplo de Saída

### Análise Comparativa (main.py)

```
================================================================================
                    STAIRCASE PROBLEM - ANÁLISE COMPARATIVA
================================================================================
...
```

### Benchmark (benchmark.py)

```
================================================================================
                    BENCHMARK - STAIRCASE PROBLEM
================================================================================

Configuração:
  • Número de execuções por teste: 30
  • Métrica principal: MEDIANA
  • Conjunto de dados: inputs.txt

Tamanhos das escadas (inputs.txt): [100, 1000, 10000]

N = 100:
  Executando 30 vezes... 10 20 30 ✓
  → Mediana Tempo: 408.32 µs
  → Mediana Memória: 3.84 KB

...

RESULTADOS DO BENCHMARK (MEDIANA)
+-------+-------------------+---------------------+-----------------+
|     N | Tempo (Mediana)   | Memória (Mediana)   | Tempo (Média)   |
+=======+===================+=====================+=================+
|   100 | 408.32 µs         | 3.84 KB             | 412.35 µs       |
+-------+-------------------+---------------------+-----------------+
|  1000 | 14.05 ms          | 81.91 KB            | 14.11 ms        |
+-------+-------------------+---------------------+-----------------+
| 10000 | 177.03 ms         | 4.77 MB             | 177.46 ms       |
+-------+-------------------+---------------------+-----------------+

✓ Resultados detalhados salvos em: benchmark_results.txt
✓ Resultados salvos em CSV: benchmark_results.csv
```

## 🔬 Análise de Complexidade

### Staircase Problem

O problema segue a seguinte relação de recorrência:
- `f(n) = f(n-1) + f(n-2)`
- Casos base: `f(1) = 1`, `f(2) = 2`

Esta é a sequência de Fibonacci modificada!

| Abordagem | Tempo | Espaço | Adequado para |
|-----------|-------|--------|---------------|
| Recursão Pura | O(2^n) | O(n) | n ≤ 35 |
| DP Bottom-up | O(n) | O(n) | Qualquer n |

## 📝 Módulos

### dpclimb.py
Contém implementações usando Programação Dinâmica:
- `climb_stairs_dp(n)` - Bottom-up com tabela completa

### recursiveclimb.py
Contém implementações recursivas:
- `climb_stairs_recursive(n)` - Recursão pura

### executiontime.py
Ferramentas para medição de tempo:
- `measure_execution_time(func, *args)` - Mede tempo de execução
- `format_time(seconds)` - Formata tempo em unidades legíveis

### memoryconsumer.py
Ferramentas para medição de memória:
- `measure_memory(func, *args)` - Mede consumo de memória
- `format_memory(bytes)` - Formata memória em unidades legíveis

### datasheet.py
Gerenciamento de dados de desempenho:
- `DataSheet` - Classe para coletar e exibir resultados
- Exportação para CSV
- Geração de resumos estatísticos

### main.py
Programa principal que orquestra todos os módulos

## 🎓 Conceitos Aplicados

- **Programação Dinâmica**: Técnica de otimização que resolve problemas complexos dividindo-os em subproblemas mais simples
- **Memoização**: Armazenamento de resultados de chamadas de função para evitar recálculos
- **Bottom-up vs Top-down**: Duas abordagens para aplicar programação dinâmica
- **Otimização de Espaço**: Redução do uso de memória mantendo apenas dados necessários

## 👥 Equipe

[Adicione os nomes dos membros da equipe aqui]

## 📄 Licença

Este projeto foi desenvolvido para fins acadêmicos na disciplina de Projeto e Análise de Algoritmos (PAA).
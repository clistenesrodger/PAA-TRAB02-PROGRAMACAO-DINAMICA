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
├── generate_graphs.py   # 📈 Gerador de gráficos (visualização)
├── examples.py          # 📚 Exemplos de uso
└── test_staircase.py    # ✅ Testes unitários
```

## 🎯 Implementações Principais

Projeto simplificado: mantidas apenas as duas abordagens solicitadas.

### 1. **ABORDAGEM RECURSIVA (Força Bruta)**
   - Arquivo: `recursiveclimb.py`
   - Função: `climb_stairs_recursive(n)`
   - Método: Recursão pura sem otimização
   - Complexidade de Tempo: **O(φⁿ)** onde φ ≈ 1.618 (exponencial)
   - Complexidade de Espaço: O(n) - pilha de recursão
   - **Adequado para**: N ≤ 40

### 2. **PROGRAMAÇÃO DINÂMICA (Bottom-up)**
   - Arquivo: `dpclimb.py`
   - Função: `climb_stairs_dp(n)`
   - Método: Tabulação de baixo para cima
   - Complexidade de Tempo: **O(n)** (linear)
   - Complexidade de Espaço: O(n) - tabela dp[]
   - **Adequado para**: Qualquer N

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
# Usa conjunto de dados do inputs.txt
python benchmark.py

# Personalizar número de execuções (ex: 50)
python benchmark.py 50
```

**Medição de Tempo Real (uma única execução):**
```bash
# Medir força bruta
python measure_realtime.py --algo brute -n 30 --repeat 3

# Medir DP bottom-up
python measure_realtime.py --algo dp -n 1000 --repeat 3

# Usar valores do inputs.txt
python measure_realtime.py --algo dp --from-inputs
```

**Executar Testes Unitários:**
```bash
python test_staircase.py
```

**Ver Exemplos de Uso:**
```bash
python examples.py
```

**Gerar Gráficos (análise visual):**
```bash
# Gera gráficos a partir do benchmark_results.csv
python generate_graphs.py

# Ou especificar arquivo CSV
python generate_graphs.py benchmark_results.csv
```
> Gera 3 gráficos:
> - `grafico_tempo.png` - Barras comparando tempo de execução
> - `grafico_memoria.png` - Linhas comparando consumo de memória  
> - `grafico_speedup.png` - Barras mostrando speedup (quantas vezes DP é mais rápido)

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
| Recursão Pura | O(φⁿ)* | O(n) | n ≤ 40 |
| DP Bottom-up | O(n) | O(n) | Qualquer n |

\* *φ ≈ 1.618 (Golden Ratio) - crescimento exponencial*

## 📊 Resultados Empíricos (Benchmark)

### Comparação de Desempenho (30 execuções, mediana)

| N | Força Bruta | DP Bottom-up | Speedup |
|---|-------------|--------------|---------|
| 10 | 8.45 µs | 20.53 µs | 0.4x |
| 20 | 925.74 µs | 53.15 µs | **17.4x** |
| 30 | 114.86 ms | 109.41 µs | **1.050x** |
| 35 | 1.27 s | 139.41 µs | **9.090x** |
| 41 | 22.71 s | 168.08 µs | **135.134x** |

### 🔥 Observações Principais:

1. **Crescimento Exponencial da Força Bruta:**
   - N=10→20: tempo aumenta **~109x**
   - N=20→30: tempo aumenta **~124x**
   - N=35→41: tempo aumenta **~18x**
   
2. **Crescimento Linear da DP:**
   - Tempo aumenta proporcionalmente a N
   - Consistente e previsível
   
3. **Ponto de Virada:**
   - Para **N ≤ 10**: Força bruta é competitiva
   - Para **N ≥ 20**: DP domina completamente

4. **Escalabilidade:**
   - **N=50** (projeção): Força bruta ~30 minutos, DP ~250 µs
   - **Speedup estimado**: ~7.200.000x

### 💾 Consumo de Memória

Ambos os algoritmos usam memória O(n):
- **Força Bruta**: Pilha de recursão (320-512 bytes para N=30-41)
- **DP Bottom-up**: Tabela dp[] (864-1304 bytes para N=30-41)
- **Diferença**: DP usa ~2.5x mais memória (desprezível para N < 1000)

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

- **Programação Dinâmica**: Técnica de otimização que resolve problemas complexos dividindo-os em subproblemas mais simples e armazenando resultados intermediários
- **Bottom-up (Tabulação)**: Construção da solução de baixo para cima, preenchendo uma tabela
- **Recursão**: Abordagem que resolve o problema chamando a si mesma com subproblemas menores
- **Análise de Complexidade**: Estudo teórico e empírico do crescimento do tempo e memória

## 🔍 Arquivos Gerados

Após executar o benchmark, os seguintes arquivos são criados:

- `benchmark_results.txt` - Resultados detalhados formatados
- `benchmark_results.csv` - Dados em CSV (tempo em segundos, memória em bytes)
  - Formato: Algoritmo, N, Mediana_Tempo_s, Media_Tempo_s, etc.
  - Ideal para análise em Excel, Python (pandas), R, etc.

### 📈 Gráficos Gerados (generate_graphs.py)

Após executar `python generate_graphs.py`:

- `grafico_tempo.png` - **Gráfico de barras** comparando tempo de execução
  - Eixo Y em escala logarítmica (crescimento exponencial vs linear)
  - Rótulos formatados (µs, ms, s)
  
- `grafico_memoria.png` - **Gráfico de linhas** comparando consumo de memória
  - Mostra crescimento linear de ambos os algoritmos
  - Rótulos formatados (B, KB, MB)

## 🎯 Recomendações de Uso

- **Para N ≤ 15**: Ambas as abordagens são aceitáveis
- **Para 15 < N ≤ 40**: DP é **dezenas a milhares de vezes** mais rápida
- **Para N > 40**: Use **apenas DP** (força bruta é inviável)

## 👥 Equipe

[Clístenes Rodger e Victor Luz]

## 📄 Licença

Este projeto foi desenvolvido para fins acadêmicos na disciplina de Projeto e Análise de Algoritmos (PAA).
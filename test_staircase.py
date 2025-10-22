"""
Testes Unitários para o Staircase Problem

Execute com: python -m pytest test_staircase.py -v
ou: python test_staircase.py
"""

import unittest
from dpclimb import climb_stairs_dp
from recursiveclimb import climb_stairs_recursive
from executiontime import measure_execution_time, format_time
from memoryconsumer import measure_memory, format_memory
from datasheet import DataSheet


class TestStaircaseSolutions(unittest.TestCase):
    """Testa as soluções do problema da escada."""
    
    def test_casos_base(self):
        """Testa os casos base."""
        # n = 0
        self.assertEqual(climb_stairs_dp(0), 0)
        # otimizado removido
        
        # n = 1
        self.assertEqual(climb_stairs_recursive(1), 1)
        self.assertEqual(climb_stairs_dp(1), 1)
        # otimizado removido
        
        # n = 2
        self.assertEqual(climb_stairs_recursive(2), 2)
        self.assertEqual(climb_stairs_dp(2), 2)
        # otimizado removido
    
    def test_valores_pequenos(self):
        """Testa com valores pequenos."""
        test_cases = [
            (3, 3),
            (4, 5),
            (5, 8),
            (6, 13),
            (7, 21),
            (8, 34),
            (9, 55),
            (10, 89)
        ]
        
        for n, expected in test_cases:
            with self.subTest(n=n):
                self.assertEqual(climb_stairs_recursive(n), expected)
                self.assertEqual(climb_stairs_dp(n), expected)
    
    def test_valores_medios(self):
        """Testa com valores médios (recursão pura seria lenta)."""
        test_cases = [
            (15, 987),
            (20, 10946),
            (25, 121393),
            (30, 1346269)
        ]
        
        for n, expected in test_cases:
            with self.subTest(n=n):
                self.assertEqual(climb_stairs_dp(n), expected)
    
    def test_valores_grandes(self):
        """Testa com valores grandes."""
        n = 100
        expected = 573147844013817084101
        
        self.assertEqual(climb_stairs_dp(n), expected)
    
    def test_consistencia_entre_metodos(self):
        """Verifica se todos os métodos retornam o mesmo resultado."""
        for n in range(1, 31):
            with self.subTest(n=n):
                result_dp = climb_stairs_dp(n)
                result_rec = climb_stairs_recursive(n)
                self.assertEqual(result_dp, result_rec)
    
    def test_relacao_fibonacci(self):
        """Verifica que a sequência segue o padrão de Fibonacci."""
        # A sequência é: 1, 2, 3, 5, 8, 13, 21, 34, 55, 89...
        # Que é similar a Fibonacci mas com valores iniciais diferentes
        # Testa se segue a relação f(n) = f(n-1) + f(n-2)
        for n in range(3, 21):
            with self.subTest(n=n):
                result_n = climb_stairs_dp(n)
                result_n1 = climb_stairs_dp(n - 1)
                result_n2 = climb_stairs_dp(n - 2)
                self.assertEqual(result_n, result_n1 + result_n2)


class TestExecutionTime(unittest.TestCase):
    """Testa o módulo de medição de tempo."""
    
    def test_measure_execution_time(self):
        """Testa a medição de tempo de execução."""
        result, exec_time = measure_execution_time(climb_stairs_dp, 10)
        
        self.assertEqual(result, 89)
        self.assertIsInstance(exec_time, float)
        self.assertGreater(exec_time, 0)
    
    def test_format_time(self):
        """Testa a formatação de tempo."""
        self.assertIn("ns", format_time(0.0000000001))
        self.assertIn("µs", format_time(0.000001))
        self.assertIn("ms", format_time(0.001))
        self.assertIn("s", format_time(1.0))


class TestMemoryConsumer(unittest.TestCase):
    """Testa o módulo de medição de memória."""
    
    def test_measure_memory(self):
        """Testa a medição de memória."""
        result, memory = measure_memory(climb_stairs_dp, 10)
        
        self.assertEqual(result, 89)
        self.assertIsInstance(memory, int)
        self.assertGreaterEqual(memory, 0)
    
    def test_format_memory(self):
        """Testa a formatação de memória."""
        self.assertIn("B", format_memory(100))
        self.assertIn("KB", format_memory(2048))
        self.assertIn("MB", format_memory(2 * 1024 * 1024))


class TestDataSheet(unittest.TestCase):
    """Testa a classe DataSheet."""
    
    def setUp(self):
        """Configura cada teste."""
        self.datasheet = DataSheet()
    
    def test_add_record(self):
        """Testa adição de registros."""
        self.datasheet.add_record("Test", 10, 89, 0.001, 1024)
        self.assertEqual(len(self.datasheet.data), 1)
        self.assertEqual(self.datasheet.data[0]['algorithm'], "Test")
        self.assertEqual(self.datasheet.data[0]['n'], 10)
    
    def test_get_summary(self):
        """Testa geração de resumo."""
        self.datasheet.add_record("Algo1", 10, 89, 0.001, 1024)
        self.datasheet.add_record("Algo1", 20, 10946, 0.002, 2048)
        self.datasheet.add_record("Algo2", 10, 89, 0.0005, 512)
        
        summary = self.datasheet.get_summary()
        
        self.assertIn("Algo1", summary)
        self.assertIn("Algo2", summary)
        self.assertEqual(summary["Algo1"]["count"], 2)
        self.assertEqual(summary["Algo2"]["count"], 1)


class TestPerformanceComparison(unittest.TestCase):
    """Testa comparações de desempenho."""
    
    def test_dp_faster_than_recursion(self):
        """Verifica que DP é mais rápido que recursão pura."""
        n = 30
        
        _, time_rec = measure_execution_time(climb_stairs_recursive, n)
        _, time_dp = measure_execution_time(climb_stairs_dp, n)
        
        # DP deve ser significativamente mais rápido
        self.assertLess(time_dp, time_rec / 10)


def run_tests():
    """Executa todos os testes."""
    # Criar um test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Adicionar todos os testes
    suite.addTests(loader.loadTestsFromTestCase(TestStaircaseSolutions))
    suite.addTests(loader.loadTestsFromTestCase(TestExecutionTime))
    suite.addTests(loader.loadTestsFromTestCase(TestMemoryConsumer))
    suite.addTests(loader.loadTestsFromTestCase(TestDataSheet))
    suite.addTests(loader.loadTestsFromTestCase(TestPerformanceComparison))
    
    # Executar os testes
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    return result.wasSuccessful()


if __name__ == "__main__":
    print("="*70)
    print("EXECUTANDO TESTES UNITÁRIOS - STAIRCASE PROBLEM")
    print("="*70)
    print()
    
    success = run_tests()
    
    print()
    print("="*70)
    if success:
        print("✓ TODOS OS TESTES PASSARAM!")
    else:
        print("✗ ALGUNS TESTES FALHARAM!")
    print("="*70)

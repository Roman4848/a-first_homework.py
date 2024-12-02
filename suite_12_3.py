import unittest
from tests_12_3 import RunnerTest, TournamentTest

# Создаем тестовый набор
suite = unittest.TestSuite()

# Добавляем тесты из классов RunnerTest и TournamentTest
suite.addTests(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))
suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))

# Запускаем тесты с verbosity=2
runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)
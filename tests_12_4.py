import logging
import unittest

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    filename='runner_tests.log',
    filemode='w',
    encoding='utf-8',
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class RunnerTest(unittest.TestCase):
    def test_walk_with_negative_speed(self):
        with self.assertRaises(ValueError):
            runner = Runner('Test Runner', -10)  # Передаем отрицательное значение
            logging.warning("Неверная скорость для Runner")
        logging.info('"test_walk_with_negative_speed" выполнен успешно')

    def test_run_with_invalid_name(self):
        with self.assertRaises(TypeError):
            runner = Runner(12345, 10)  # Передаем что-то кроме строки
            logging.warning("Неверный тип данных для объекта Runner")
        logging.info('"test_run_with_invalid_name" выполнен успешно')


if __name__ == '__main__':
    unittest.main()
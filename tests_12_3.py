import unittest


def skip_if_frozen(test_func):
    def wrapper(self, *args, **kwargs):
        if getattr(self, 'is_frozen', False):
            self.skipTest('Тесты в этом кейсе заморожены')
        return test_func(self, *args, **kwargs)
    return wrapper


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @skip_if_frozen
    def test_challenge(self):
        self.assertEqual(1, 1)

    @skip_if_frozen
    def test_run(self):
        self.assertEqual(2, 2)

    @skip_if_frozen
    def test_walk(self):
        self.assertEqual(3, 3)


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @skip_if_frozen
    def test_first_tournament(self):
        self.assertEqual(4, 4)

    @skip_if_frozen
    def test_second_tournament(self):
        self.assertEqual(5, 5)

    @skip_if_frozen
    def test_third_tournament(self):
        self.assertEqual(6, 6)


def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(RunnerTest))
    test_suite.addTest(unittest.makeSuite(TournamentTest))
    return test_suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())
# runner.py
class Runner:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def __eq__(self, other):
        return self.name == other.name

    def __hash__(self):
        return hash(self.name)

    def run(self, distance):
        return distance / self.speed

    def walk(self, distance):
        return distance / (self.speed / 2)

class Tournament:
    def __init__(self, distance, runners):
        self.distance = distance
        self.runners = runners

    def start(self):
        results = {}
        for runner in self.runners:
            time = runner.run(self.distance)
            results[runner] = time
        sorted_results = sorted(results.items(), key=lambda x: x[1])
        return {i + 1: runner.name for i, (runner, _) in enumerate(sorted_results)}


import unittest

class TournamentTest(unittest.TestCase):
    all_results = {}

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = Runner("Усэйн", 10)
        self.runner2 = Runner("Андрей", 9)
        self.runner3 = Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for key in sorted(cls.all_results.keys()):
            print(cls.all_results[key])

    def test_tournament_usain_nik(self):
        tournament = Tournament(90, [self.runner1, self.runner3])
        results = tournament.start()
        self.all_results[len(self.all_results) + 1] = results
        self.assertTrue(results[max(results.keys())] == "Ник")

    def test_tournament_andrey_nik(self):
        tournament = Tournament(90, [self.runner2, self.runner3])
        results = tournament.start()
        self.all_results[len(self.all_results) + 1] = results
        self.assertTrue(results[max(results.keys())] == "Ник")

    def test_tournament_usain_andrey_nik(self):
        tournament = Tournament(90, [self.runner1, self.runner2, self.runner3])
        results = tournament.start()
        self.all_results[len(self.all_results) + 1] = results
        self.assertTrue(results[max(results.keys())] == "Ник")

if __name__ == "__main__":
    unittest.main()
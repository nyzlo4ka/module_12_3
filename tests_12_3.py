import unittest
import runner_and_tournament
import runner


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены.')
    def test_walk(self):
        run1 = runner.Runner('Max')
        for _ in range(10):
            run1.walk()
        self.assertEqual(run1.distance, 50, f'{run1.name} ran {run1.distance}m, but should have done 50m')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены.')
    def test_run(self):
        run2 = runner.Runner('Dan')
        for _ in range(10):
            run2.run()
        self.assertEqual(run2.distance, 100, f'{run2.name} ran {run2.distance}m, but should have done 100m')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены.')
    def test_challenge(self):
        run1 = runner.Runner('Max')
        run2 = runner.Runner('Dan')
        for _ in range(10):
            run1.run()
            run2.walk()
        self.assertNotEqual(run1.distance, run2.distance)


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        TournamentTest.all_results = {}

    def setUp(self):
        self.run1 = runner_and_tournament.Runner('Усэйн', 10)
        self.run2 = runner_and_tournament.Runner('Андрей', 9)
        self.run3 = runner_and_tournament.Runner('Ник', 3)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены.')
    def test_tournament1(self):
        res1 = runner_and_tournament.Tournament(90, self.run1, self.run3)
        TournamentTest.all_results = res1.start()
        self.assertTrue(TournamentTest.all_results[2] == 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены.')
    def test_tournament2(self):
        res2 = runner_and_tournament.Tournament(90, self.run2, self.run3)
        TournamentTest.all_results = res2.start()
        self.assertTrue(TournamentTest.all_results[2] == 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены.')
    def test_tournament3(self):
        res3 = runner_and_tournament.Tournament(90, self.run1, self.run2, self.run3)
        TournamentTest.all_results = res3.start()
        self.assertTrue(TournamentTest.all_results[3] == 'Ник')

    def tearDown(self):
        for k, v in TournamentTest.all_results.items():
            print(f'{k}: {v}, ', end='')
        print()


if __name__ == '__main__':
    unittest.main()

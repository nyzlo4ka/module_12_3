import unittest
import tests_12_3

tournamentST = unittest.TestSuite()
tournamentST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
tournamentST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))

run = unittest.TextTestRunner(verbosity=2)
run.run(tournamentST)

# test_challenge (tests_12_3.RunnerTest.test_challenge) ... ok
# test_run (tests_12_3.RunnerTest.test_run) ... ok
# test_walk (tests_12_3.RunnerTest.test_walk) ... ok
# test_tournament1 (tests_12_3.TournamentTest.test_tournament1) ... skipped 'Тесты в этом кейсе заморожены.'
# test_tournament2 (tests_12_3.TournamentTest.test_tournament2) ... skipped 'Тесты в этом кейсе заморожены.'
# test_tournament3 (tests_12_3.TournamentTest.test_tournament3) ... skipped 'Тесты в этом кейсе заморожены.'
# ----------------------------------------------------------------------
# Ran 6 tests in 0.000s
# OK (skipped=3)

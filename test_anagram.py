import unittest
from anagram import lag_noekkel, finn_anagrammer

# Enhetstester for metodene i anagram.py


class TestAnagram(unittest.TestCase):

    def test_lag_noekkel(self):

        self.assertEqual(lag_noekkel("arne"), lag_noekkel("rane"))

        # sjekker at det ikke skilles mellom store og smaa bokstaver
        self.assertEqual(lag_noekkel("Jan"), lag_noekkel("jan"))

        # sjekker at mellomrom ignoreres
        self.assertEqual(lag_noekkel("Per"), lag_noekkel(" P e  R "))

    def test_finn_anagrammer(self):

        liste_a = ["Kåre", "åker", "Lise", "Lisa"]
        forventet_a = [{"Kåre", "åker"}]

        self.assertEqual(finn_anagrammer(liste_a), forventet_a)

        # sjekker at duplikater ignoreres
        liste_b = ["Per", "Dina", "Per"]
        forventet_b = []

        self.assertEqual(finn_anagrammer(liste_b), forventet_b)

        # stoerre test, hver linje er anagrammer av hverandre

        liste_c = ["airmen", "marine", "remain",
                   "asleep", "elapse", "please",
                   "ate", "eat",
                   "canter", "nectar", "trance"]

        self.assertEqual(len(finn_anagrammer(liste_c)), 4)


if __name__ == '__main__':
    unittest.main()

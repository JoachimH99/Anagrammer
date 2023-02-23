from anagram import lag_noekkel, finn_anagrammer

# Enhetstester for metodene i anagram.py


def test_lag_noekkel():

    assert lag_noekkel("arne") == lag_noekkel("rane")

    # sjekker at det ikke skilles mellom store og smaa bokstaver
    assert lag_noekkel("Jan") == lag_noekkel("jan")

    # sjekker at mellomrom ignoreres
    assert lag_noekkel("Per") == lag_noekkel(" P e  R ")


def test_finn_anagrammer():

    liste_a = ["Kåre", "åker", "Lise", "Lisa"]
    forventet_a = [{"Kåre", "åker"}]

    assert finn_anagrammer(liste_a) == forventet_a

    # sjekker at duplikater ignoreres
    liste_b = ["Per", "Dina", "Per"]
    forventet_b = []

    assert finn_anagrammer(liste_b) == forventet_b

    # stoerre test, hver linje er anagrammer av hverandre

    liste_c = ["airmen", "marine", "remain",
               "asleep", "elapse", "please",
               "ate", "eat",
               "canter", "nectar", "trance"]

    assert len(finn_anagrammer(liste_c)) == 4

import pyarrow.parquet as pq
from collections import defaultdict

# KJOERETIDSKOMPLEKSITET:
# Dersom vi antar at lengden paa navnene i input ikke vokser, vil
# kjoeretidskompleksiteten av finn_anagrammer() vaere i O(n)


def lag_noekkel(streng):
    """ Lager en noekkel for en gitt streng som er lik for alle ord som er
        anagrammer av hverandre.

    Argumenter:
        streng (string): en string som en noekkel skal genereres for.

    Returverdi:
        string: en noekkel.

    """

    noekkel = streng.lower()
    noekkel = ''.join(sorted(noekkel))
    return noekkel.replace(' ', '')


def finn_anagrammer(liste):
    """ Finner alle ord som er anagrammer av hverandre i en liste.

    Argumenter:
        liste (list(string)): en liste med strenger.

    Returverdi:
        list(set(string)): en liste med sett hvor elementene i hvert
        sett er anagrammer av hverandre.

    """

    anagram_dict = defaultdict(set)

    for ord in liste:
        ord = str(ord)

        # alle ord som gir samme noekkel legges i samme sett
        noekkel = lag_noekkel(ord)
        anagram_dict[noekkel].add(ord)

    # alle sett hvor det har blitt funnet anagrammer (|set| > 1)
    # blir lagt i resultat
    resultat = []

    for noekkel in anagram_dict:
        if len(anagram_dict[noekkel]) > 1:
            resultat.append(anagram_dict[noekkel])

    return resultat


def print_resultat(resultat):
    """ Skriver ut hvert elementene fra hvert sett i resultat,
        eller en melding dersom resultat er en tom liste.

    Argumenter:
        liste (list(set(string))): en liste med sett av strenger.

    Returverdi:
        None

    """

    if len(resultat) == 0:
        print("Ingen anagrammer funnet")

    else:
        print("Anagrammer:")
        
        teller = 1
        for sett in resultat:
            liste = list(sett)
            ut = f'{teller}: {liste[0]}'

            for navn in liste[1:]:
                ut += f', {navn}'

            print(ut)
            teller += 1


def main():

    tabell = pq.read_table("population.parquet")

    resultat = finn_anagrammer(tabell[0])

    print_resultat(resultat)


if __name__ == '__main__':
    main()

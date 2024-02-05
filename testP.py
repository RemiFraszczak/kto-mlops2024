import unittest
"""
Count names with more than seven letters
"""
def Superieur_a_sept(prenoms_a_tester):
    longueur_min = 7 
    more_than_seven = 0
    for le_prenom_a_tester in prenoms_a_tester:
        "On test chaque prenom si la taille du mot est supérieur ou inférieur à 7 lettres"
        if len(le_prenom_a_tester) > longueur_min:
            more_than_seven += 1
            print("Prenom supérieur à 7 lettres: " + le_prenom_a_tester)
        else:
            print("Prenom inférieur ou égal à 7 lettres: " + le_prenom_a_tester)
    return more_than_seven

class TestNamesMethod(unittest.TestCase):
     def test_names(self):
        prenoms = ["Guillaume", "Gilles", "Juliette", "Antoine", "François", "Cassandre"]
        more_than_seven = Superieur_a_sept(prenoms)
        print("\nNombre de prénoms supérieurs à 7 lettres: " + str(more_than_seven))
        self.assertEqual(more_than_seven, 4)

if __name__ == '__main__':
    unittest.main()
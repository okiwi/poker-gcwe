import unittest

from jeu import Jeu
from joueur import Joueur


class TestJoueur(unittest.TestCase):
    def test_a_un_nom(self):
        david = Joueur('David')
        self.assertEqual('David', david.nom)


class TestJeu(unittest.TestCase):
    def setUp(self):
        self.jeu = Jeu()
        self.joueurs = [Joueur('David'), Joueur('Guillaume'), Joueur('Damien'), Joueur('Mathieu')]
        self.jeu.ajoute_des_joueurs(self.joueurs)

    def test_peut_créer_un_jeu(self):
        self.assertTrue(self.jeu)

    def test_peut_ajouter_des_joueurs_en_plusieurs_fois(self):
        self.assertEqual(len(self.jeu.joueurs), 4)
        self.assertEqual(self.jeu.joueurs, self.joueurs)
        self.jeu.ajoute_des_joueurs(['Edouard'])
        self.assertEqual(len(self.jeu.joueurs), 5)

    def test_le_premier_joueur_est_le_dealer(self):
        self.assertEqual('David', self.jeu.donne_dealer().nom)

    def test_chaque_joueur_joue_tour_a_tour(self):
        self.assertEqual('David', self.jeu.donne_joueur().nom)
        self.jeu.tour_suivant()
        self.assertEqual('Guillaume', self.jeu.donne_joueur().nom)
        self.jeu.tour_suivant()
        self.jeu.tour_suivant()
        self.jeu.tour_suivant()
        self.assertEqual('David', self.jeu.donne_joueur().nom)

    def test_le_joueur_peut_passer_son_tour(self):
        self.jeu.action('passe')
        self.assertEqual(len(self.jeu.joueurs_restant), 3)
        self.assertTrue(self.joueurs[0] not in self.jeu.joueurs_restant)

    def test_le_joueur_peut_checker(self):
        self.jeu.action('check')
        self.assertEqual(len(self.jeu.joueurs_restant), 4)
        self.assertTrue(self.joueurs[0] in self.jeu.joueurs_restant)

    def test_a_un_gagnant(self):
        self.jeu.action('passe')
        self.assertIsNone(self.jeu.gagnant())
        self.jeu.action('passe')
        self.jeu.action('passe')
        self.assertEqual('Mathieu', self.jeu.gagnant().nom)

    def test_chaque_joueur_se_voit_attribuer_2_cartes(self):
        self.jeu.deal()
        for joueur in self.joueurs:
            self.assertEqual(len(joueur.cartes), 2)

    def test_deux_joueurs_ne_peuvent_pas_avoir_la_meme_main(self):
        self.jeu.deal()
        self.assertTrue(self.joueurs[0].cartes[0] not in self.joueurs[1].cartes)
        self.assertTrue(self.joueurs[0].cartes[1] not in self.joueurs[1].cartes)

    def test_un_jeu_a_52_cartes(self):
        self.assertEqual(52, len(self.jeu.cartes))



from random import randrange


class Jeu:
    def __init__(self):
        self.joueurs_restant = []
        self.joueurs = []
        self.position = 0
        couleurs = ['h', 's', 'c', 'd']
        valeurs = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.cartes = []
        for valeur in valeurs:
            for couleur in couleurs:
                self.cartes.append(valeur + couleur)

    def ajoute_des_joueurs(self, joueurs):
        for joueur in joueurs:
            self.joueurs.append(joueur)
        self.joueurs_restant = self.joueurs

    def donne_dealer(self):
        return self.joueurs[0]

    def donne_joueur(self):
        if self.position >= len(self.joueurs):
            self.position = 0

        return self.joueurs[self.position]

    def tour_suivant(self):
        self.position += 1

    def action(self, action):
        if action == 'passe':
            self.joueurs.pop(0)

    def gagnant(self):
        if len(self.joueurs_restant) == 1:
            return self.joueurs_restant[0]

    def _donne_moi_une_carte(self):
        return self.cartes_restantes.pop(randrange(len(self.cartes_restantes)))

    def deal(self):
        self.cartes_restantes = self.cartes
        for joueur in self.joueurs:
            joueur.cartes = [self._donne_moi_une_carte(), self._donne_moi_une_carte()]

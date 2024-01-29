from broly import *
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

class Gojo(Ennemi):
    def collecter_donnees(self, etat_jeu):
        # Collecte les données pertinentes pour l'entraînement
        donnees = {
            'position_x': self.x,
            'position_y': self.y,
            'etat_jeu': etat_jeu
            # Ajoutez d'autres données si nécessaire
        }
        return donnees
    
    def entrainer_modele(self, X_train, y_train):
        # Entraîne un modèle d'apprentissage machine sur les données fournies
        model = LinearRegression()
        model.fit(X_train, y_train)
        return model
    
    def predire_action(self, modele, donnees):
        # Prédit l'action à partir des données fournies en utilisant le modèle entraîné
        X = np.array(donnees).reshape(1, -1)  # Convertit les données en tableau numpy
        action_predite = modele.predict(X)
        return action_predite

    def deplacer(self, etat_jeu):
        # Collecte les données
        donnees = self.collecter_donnees(etat_jeu)

        # Chargez les données d'entraînement depuis un fichier CSV ou générez-les directement dans le jeu

        # Entraînez un modèle d'apprentissage machine (par exemple, Linear Regression)
        X_train, X_test, y_train, y_test = train_test_split(self.x, self.y, test_size=0.2, random_state=42)
        modele = self.entrainer_modele(X_train, y_train)

        # Prédit l'action à partir des données
        action_predite = self.predire_action(modele, donnees)

        # Exécute l'action prédite (par exemple, déplace Gojo)
        self.execute_action(action_predite)

    def execute_action(self, action):
        # Exécute l'action prédite
        # Par exemple, déplace Gojo en fonction de l'action prédite
        if action == 'gauche':
            self.x -= 1
        elif action == 'droite':
            self.x += 1
        elif action == 'haut':
            self.y -= 1
        elif action == 'bas':
            self.y += 1


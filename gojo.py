from broly import *
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

class Gojo(Ennemi):
    def collecter_donnees(self, etat_jeu):
        
        donnees = {
            'position_x': self.x,
            'position_y': self.y,
            'etat_jeu': etat_jeu
            
        }
        return donnees
    
    def entrainer_modele(self, X_train, y_train):
        
        model = LinearRegression()
        model.fit(X_train, y_train)
        return model
    
    def predire_action(self, modele, donnees):
        
        X = np.array(donnees).reshape(1, -1) 
        action_predite = modele.predict(X)
        return action_predite

    def deplacer(self, etat_jeu):
        
        donnees = self.collecter_donnees(etat_jeu)

        data = np.genfromtxt('donnees_partie.csv', delimiter=',', skip_header=1)
        X_train = data[:, :-1]
        y_train = data[:, -1]

        
        modele = self.entrainer_modele(X_train, y_train)

        
        action_predite = self.predire_action(modele, donnees)

        
        self.execute_action(action_predite)

    def execute_action(self, action):
        
        if action == 'gauche':
            self.x -= 1
        elif action == 'droite':
            self.x += 1
        elif action == 'haut':
            self.y -= 1
        elif action == 'bas':
            self.y += 1


import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split, GridSearchCV
# Importer les données
data = pd.read_csv("donnees_partie.csv")

# Séparer les données d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(data, data["gojo_score"], test_size=0.25)

# Créer le modèle
model = LinearRegression()

# Définir les hyperparamètres à tester
param_grid = {
    'fit_intercept': [True, False],
    'normalize': [True, False]
}

# Recherche des meilleurs hyperparamètres
grid_search = GridSearchCV(model, param_grid, cv=5)
grid_search.fit(X_train, y_train)

# Obtenir le meilleur modèle
best_model = grid_search.best_estimator_

# Entraîner le meilleur modèle
best_model.fit(X_train, y_train)

# Évaluer le modèle
score = best_model.score(X_test, y_test)

print("Score du modèle :", score)


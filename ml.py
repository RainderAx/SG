import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

# Importer les données
data = pd.read_csv("data.csv")

# Séparer les données d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(data, data["target"], test_size=0.25)

# Créer le modèle
model = LinearRegression()

# Entraîner le modèle
model.fit(X_train, y_train)

# Évaluer le modèle
score = model.score(X_test, y_test)

print("Score du modèle :", score)
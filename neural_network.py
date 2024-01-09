#NEURAL NETWORK
#Multi layer librairy used
from sklearn.datasets import fetch_openml
from sklearn.neural_network import MLPClassifier

import joblib

import data

multi_layer = MLPClassifier(hidden_layer_sizes=(100,100,100,100,100,), max_iter=200, alpha=1e-4,
                        solver='sgd', tol=1e-4, random_state=1,
                        learning_rate_init=.1)

def train():

    multi_layer.fit(data.image_train, data.label_train)
    print("Training set score: %f" % multi_layer.score(data.image_train, data.label_train))
    print("Test set score: %f" % multi_layer.score(data.image_train, data.label_train))

    joblib.dump(multi_layer, "trained_model.joblib")

def load():
    try:
        multi_layer=joblib.load('trained_model.joblib')
        print("Modèle chargé")
        return multi_layer
    except FileNotFoundError:
        print("Pas de modèle entrainé trouvé")
        return None
    
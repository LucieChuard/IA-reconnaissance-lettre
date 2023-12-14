#NEURAL NETWORK
#Data = input/output
#mise en place -ici- d'un multi layer perception neural network (MLP)

#Multi layer librairy used
from sklearn.datasets import fetch_openml
from sklearn.neural_network import MLPClassifier

import data

# create first multi layer - 1 hidden layer with 50 neurons and set to run through the data 20 times
#alpha --> ajustement de la méthode de tri, une valeur plus grande donne une courbe plus droite et plus large, et une valeur plus basse est plus fine, potentiellement plus stable, pas sure selon de contexte surement
#solver --> pour optimisation des ressouces ici ça semble être médium
#tol tolérance de l'optimisation
multi_layer1 = MLPClassifier(hidden_layer_sizes=(50,), max_iter=20, alpha=1e-4,
                    solver='sgd', verbose=10, tol=1e-4, random_state=1,
                    learning_rate_init=.1)


multi_layer1.fit(data.image_train, data.label_train)
print("Training set score: %f" % multi_layer1.score(data.image_train, data.label_train))
print("Test set score: %f" % multi_layer1.score(data.image_test, data.label_test))
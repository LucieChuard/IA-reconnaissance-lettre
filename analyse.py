import neural_network
import data
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix

valeurs_predites = neural_network.multi_layer1.predict(data.image_train)

# Visualisation des erreurs à travers la matrice de confusion
matrix_confusion = confusion_matrix(data.label_train, valeurs_predites)
plt.matshow(matrix_confusion)
plt.show()

#CONSTRUCTION DES DATAS
from emnist import extract_training_samples

image,label=extract_training_samples("letters")
#on associe les variables image et label aux fichiers importés

image=image/255

image_train, image_test=image[:60000], image[60000:70000]
label_train, label_test=label[:60000], label[60000:70000]
#définition de la zone d'entrainement de l'IA et de la zone de test

image_train=image_train.reshape(60000,784)
image_test=image_test.reshape(10000,784)
#Pour finir la préparation - on enregistre le nombre d'image dans chaque set de data et le nombre de pixels par image - ici 28*28 = 784

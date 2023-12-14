#CONSTRUCTION DES DATAS
from emnist import extract_training_samples
#emnist est une librairie de données - il y a un nombre ahurissants de lettres écrites à la main, avec différentes écritures
#Les lettres sont séparées en images, chacune nommée par la lettre associée.

image,label=extract_training_samples("letters")
#on associe des variables aux données de la fonction extract

image=image/255
#division de chaque image par 255 pour avoir des valeurs entre 0 et 1 à analyser
#les couleurs de l'image donneront des valeurs entre 0 et 1 qui seront analysées pour interpreter la lettre la plus succeptible d'être correcte

image_train, image_test=image[:60000], image[60000:70000]
label_train, label_test=label[:60000], label[60000:70000]
#définition de la zone d'entrainement de l'IA et de la zone de test

image_train=image_train.reshape(60000,784)
image_test=image_test.reshape(10000,784)
#Pour finir la préparation - on enregistre le nombre d'image dans chaque set de data et le nombre de pixels par image - ici 28*28 = 784

# Projet
L'idée est de s'entrainer à l'utilisation de l'IA par le biai d'un programme qui interprète les lettres en écriture manuscrite pour les retranscrire en entrée clavier. </br>
Par la suite, cette IA communiquera avec Word et une input en direct avec la tablette graphique pour écrire directement sur l'outil de traitement de texte.

# Principe technique de l'IA
Le programme va prendre un fichier image et le fractionner en 255 pixels. En fonction de la couleur, le logiciel va attribuer un nombre entre 1 et 255.

Chaque pixel ayant son dégradé de couleur, le programme se retrouvera avec des combinaisons spécifique pour chaque fichier.

## Phase apprentissage
Lors de la phase d'apprentissage, le programme va se concentrer sur une partie des données. Il va prendre la lettre du fichier et l'attribuer à la combinaison. Les succéssions d'écritures différentes va lui permettre d'élargir les critères et les resserer pour obtenir une sortie plus cohérente.

Ici, le programme ne propose pas encore de sortie. Il se "contente" d'apprendre et d'assimiler les différences dans les fichiers.

## Phase d'entrainement
Lors de la phase d'entrainement, le programme va prendre le reste des données. Cette fois, il détermine la lettre la plus probable selon son analyse avant de vérifier avec le label. Si c'est correct, on passe à la prochaine, autrement, le programme réajuste ses critères. 

A savoir que certaines lettres sont très proches et seront plus sujettes à erreur de la part de l'IA. (l / p)

# Librairies
* sklearn &rarr; fournis des outils de MLP
    * .dataset
        * fetch_openml
    * .neural_network
        * MLPClassifier &rarr; Création des layers
* Matplotlib pour les échantillonnages de lettres avec display visuel
* PIL &rarr; aka Pillow - Traitement d'image
    * format : PPM, PNG, JPEG, GIF, TIFF, BMP
    * Archivage d'image &rarr; création de miniature / conversion d'image
    * Affichage d'image &rarr; PIL.ImageTk (voir compatibilité windows)
    * traitement d'images &rarr; filtrage, convolution, conversion d'espaces couleurs, redimenssionement, transformation géométrique (rotation,...)

# Etapes
## 1 - Préparer les datas
### Importation
Les datas viennent d'une liste fournie par l'emnist qui regroupe  des milliers de lettres et d'écritures différentes. 

Chaque donnée a son propre fichier, lequel est étiquetté selon le caractère associé en titre qui correspond à la lettre écrite. 

### Paramétrage des données
*Fichier data.py*
Pour faciliter le traitement des données, on fractionne la couleur d'image par 255 qui permet d'avoir des couleurs plus fortes en contrast. <br>
Grace à ce nombre, il le programme va interprêté à quelle lettre cet élément correspond le plus et l'y associer.

Les données sont séparées en deux parties : celles utilisées pour l'apprentissage, et celles utilisées pour l'entrainement. (On écarte également les dernières données qui ne contiennent que des chiffres)

Il faut ensuite resize les images pour qu'elles aient toutes les même dimensions, en surface.
## 2 - Définir les réseaux neuronaux
*Fichier neural_network.py*
On définie un premier réseau neuronal. Les valeurs qui lui sont associés peuvent aisément être modifiées pour mieux coller aux besoins de précisions et de durée. 

Les RN ici sont définis par : 
* **hidden_layer_sizes** (X,) &rarr; neurones qui vont traiter les datas. Un nombre plus élevé va augmenter les scores de réussites.
* **max_iter** &rarr; nombre de fois que les neurones vont interpreter les datas. Un nombre plus grand va améliorer les scores d'entrainement.
* **alpha** &rarr; ajustement de la méthode de tri. Est ce qu'on veut une courbe droite et large (peu précis) ou une courbe plus fine potentiellement plus stable, au risque d'être trop selectif et de fausser les résultats. En fonction des besoins, on va respectivement mettre une valeur plus grande ou plus petite.
* **solver** &rarr; optimisation du "poids" de l'IA. 
    * "lbfgs" optimiseur parmi les méthodes quasi-Newton  &rarr; méthode où l'on cherche le 0 d'une fonction réelle
    * "sgd" &rarr; optimisation stochatique (par recherche aléatoire) du coefficient pour la courbe d'analyse (utilisé par défaut)
    * "adam" &rarr;  optimisation stochatique 

    **Note : quand choisir ADAM ou SGD ?** 
    *SGD semble plus adéquat sur des petites bases de données. ADAM de son côté a plus de risque d'erreur hors grande base de donnée et process au détriment des performance*
* **tol** &rarr; Par défaut 1e-4. Tolérance pour l'optimisation du programme. Quand la performance ne s'améliore pas au minimum par la valeur de tol, pendant "n_iter_no_change" nombre d'itération (par défaut 10), l'entrainement s'arrête car le programme est considéré avoir atteint sa convergence. 
* **random_state** &rarr; détermine le nombre de génération aléatoire à relancer 
* **learning_rate_init** &rarr; par défaut 0.001, représente le pas dans la mise à jour du poids. Seulement utilisé avec les solvers ADAM et SGD.

## 3 - Premiers lancés
*Fichier neural_network.py*
Grace à la commande *.fit(image, label)* on va pouvoir lancer le process d'apprentissage et d'entrainement. 

Si on fait afficher les résultats, on peut facilement voir les évolutions des performances en fonction des arguments modifiés. On remarquera aussi que les résultats sont très sensiblement différent d'un test à l'autre. 

Ainsi, les résultat de l'apprentissage seront autour d'une valeur, qui sera ajustée et améliorée par l'entrainement.

Ce process peut prendre de quelques secondes à quelques minutes selon le nombre de données, de layers, et d'itération à mettre en place.

## 4 - Créer l'affichage d'une lettre perçue
*Fichier screen.py*

L'affichage se fait avec Matlplotlib. L'idée est d'avoir un exemple de comment l'IA perçoit les images. 

* On va choisir une image au hasard dans la liste depuis data.py.
On récupère le label de l'image qu'on va print dans la console pour vérifier le résultat
* On display l'image resizée avec la commande img.reshape
* On affiche l'image

**Note** : On remarquera que des couleurs ont été mises sur l'image, comme une vision thermique. 

## 5 - Analyse des erreurs
On créer une liste avec les valeurs prédites de l'étape d'entrainement. Cette liste "valeurs_predites" va comparer les labels des lettes avec les valeurs lues et afficher les quantités de bonnes réponses pour chaque possibilités.

On va donc être capable de voir où se trouvent les erreurs les plus récurrentes et en déduire quoi faire. 

![Matrice de confusion](/image%20readme/matrice%20de%20confusion.png)

Ici, on voit une diagonale claire qui représente les bonnes reponses (voir explication MC). D'autres cases claires (bleues) se démarquent du restent. Ce sont les erreurs les plus récurrentes. 

Par exemple, 'l' et 'i' sont régulièrement confondus. C'est donc sur ça qu'on va essayer de travailler.

Si on veut analyser plus en détail, on peut faire afficher les images précises des erreurs rencontrées. 

## 6 - Amélioration des résultats
L'amélioration des résultats peut se faire en modifiant les critères du premier réseau neuronal, ou par l'ajout d'un nouveau.

**Note** Deux réseaux neuronaux iront plus vite qu'un seul avec des nombres de répétitions ou de neurones bien plus importants. C'est lié à la vitesse de calcul des processeur. 

## 7 - Préparer le système d'écriture
L'écran définissant la zone d'écriture est gérée via Tkinter, avec l'aide de PIL (pilow) pour convertir la lettre en image à sauvegarder.

Cela doit se faire via une class, avec des fonctions définies pour les différentes actions que l'on veut avoir : ici, dessiner(au maintient du bouton clic gauche - paint) et sauvegarder (au relachement du bouton clic gauche - reset)

Pour le confort visuel, l'image servant à dessiner (le canvas) est grise avec une écriture noire. Pour autant, à la sauvegarde, l'image est enregistrée (self.image) en blanc, pour que l'IA puisse traiter l'image sans difficulté.

La fonction paint va relier les coordonnées de début et de fin des zones de clic puis les relier par des courbes et des lignes.

La fonction reset va définir ce qu'il se passe lorsque l'on relache le bouton de la souris : la sauvegarde de l'image.

# Vocabulaire
* Multi layer perception neural network (MLP)
* Matrice de Confusion (MC): Matrice qui permet d'analyser les performances des prédictions, et par extension sa "confusion". Les résultats sont présentés sous forme de matrice mathématique de X,X colonnes et lignes correspondantes aux nombres de valeurs possibles. On donne un score en fonction du nombre de correctes réponses pour chaque possibilité. De cette façon, il est très facile de déterminer à quelle lettre le programme se trompe le plus. 

# Sources
Projet : 
https://colab.research.google.com/drive/1NyYH1EPpaJlMBLK0fcKYz4icaD1SNSLK#scrollTo=dWe9nrfdaPBq

**Documentation** : 
https://scikit-learn.org
https://he-arc.github.io/livre-python/pillow/index.html
https://pypi.org/project/opencv-python/ 

**Principes mathématiques** : 
* matrice de confusion : 
https://www.jedha.co/formation-ia/matrice-confusion
https://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix.html